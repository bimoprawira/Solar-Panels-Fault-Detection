from ultralytics import YOLO
import time
import streamlit as st
import cv2
from tempfile import NamedTemporaryFile
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, WebRtcMode, VideoProcessorFactory
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import settings
import torch
import time

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

def load_model(model_path):
    model = YOLO(model_path)
    if torch.cuda.is_available():
        model.to('cuda')  # Memindahkan model ke GPU jika tersedia
    return model


import streamlit as st

def notify_solution(labels):
    notification_mapping = {
        "Snow": ("Panel tertutup salju, mohon dapat dibersihkan secepatnya!", "#098eb4"),
        "Dust": ("Panel tertutup debu dan kotoran, mohon dapat dibersihkan secepatnya!", "#098eb4"),
        "Bird Drop": ("Panel terdapat tai manuk, mohon dapat dibersihkan secepatnya!", "#098eb4"),
        "Physical Damage": ("Panel rusak! Wajib Diganti jika mengalami defective. Jika tidak, panel rusak tetapi masih dapat digunakan.", "#098eb4"),
        "Defective": ("Panel rusak parah! Segera ganti untuk menghindari kerusakan lebih lanjut.", "#ebbab9"),
        "Non Defective": ("Bagus! Tetap jaga kondisi solar panel.", "#098eb4"),
    }
    for label in labels:
        if label in notification_mapping:
            message, color = notification_mapping[label]
            # Gunakan HTML untuk mengatur background
            st.markdown(
                f"""
                <div style="background-color:{color};padding:10px;border-radius:5px;">
                    <b>{message}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

def showDetectFrame(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    # Mengubah ukuran frame agar lebih kecil untuk deteksi yang lebih cepat
    small_image = cv2.resize(image, (640, 480))  # Mengubah resolusi menjadi 640x480
    res = model.predict(small_image, conf=conf)
    res_plotted = res[0].plot()
    st_frame.image(res_plotted, caption='Detected Video', channels="BGR")


def play_webcam(conf, model):
    vid_cap = cv2.VideoCapture(settings.WEBCAM_PATH)
    vid_cap.set(cv2.CAP_PROP_FPS, 45)  # Set FPS ke 30
    vid_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Resolusi lebih rendah
    vid_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    st_frame = st.empty()
    stop_button = st.button("Stop")
    while vid_cap.isOpened() and not stop_button:
        ret, frame = vid_cap.read()
        if not ret:
            break
        showDetectFrame(conf, model, st_frame, frame)
    vid_cap.release()



import av
class VideoTransformer(VideoTransformerBase):
    def __init__(self, model, conf):
        self.model = model
        self.conf = conf

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        try:
            res = self.model.predict(img, show=False, conf=self.conf)
            res_plotted = res[0].plot()
            return res_plotted
        except Exception as e:
            print("Error in transform:", e)
            return img
        

def check_camera_source(source=0):
    vid_cap = cv2.VideoCapture(source)
    if not vid_cap.isOpened():
        raise ValueError(f"Camera is not available at the source {source}")
    vid_cap.release()
    check_camera_source(settings.WEBCAM_PATH)

def live(conf, model):
    webrtc_ctx = webrtc_streamer(
        key="object-detection",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={
            "video": {"frameRate": {"ideal": 60, "max": 90}},  # Set FPS
            "audio": False
        },
        async_processing=True,
        video_processor_factory=lambda: VideoTransformer(model, conf),
    )

def process_uploaded_video(conf, model):
    uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    
    if uploaded_video is not None:
        # Menyimpan file video sementara
        with NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
            temp_file.write(uploaded_video.read())
            temp_video_path = temp_file.name
        
        # Menampilkan video menggunakan streamlit video player
        st.video(temp_video_path)  # Menambahkan pemutaran video
        
        if st.button('Deteksi'):
            try:
                # Menggunakan OpenCV untuk membaca video yang sudah disimpan sementara
                vid_cap = cv2.VideoCapture(temp_video_path)
                st_frame = st.empty()

                while vid_cap.isOpened():
                    success, image = vid_cap.read()
                    if success:
                        showDetectFrame(conf, model, st_frame, image)
                    else:
                        vid_cap.release()
                        break
            except Exception as e:
                st.error("Error loading video: " + str(e))

def process_frame_async(vid_cap, conf, model, st_frame):
    while vid_cap.isOpened():
        ret, frame = vid_cap.read()
        if not ret:
            break
        showDetectFrame(conf, model, st_frame, frame)
        time.sleep(0.03)  # Menunggu sejenak sebelum frame berikutnya diproses
        
def play_stored_video(conf, model):
    source_vid = st.selectbox("Please Select a Video from the Provided Options", settings.VIDEOS_DICT.keys())
    video_path = settings.VIDEOS_DICT.get(source_vid)
    
    if video_path is None:
        st.error("Video not found.")
        return
    
    vid_cap = cv2.VideoCapture(str(video_path))
    if not vid_cap.isOpened():
        st.error(f"Unable to open video: {video_path}")
        return
    
    st_frame = st.empty()
    while vid_cap.isOpened():
        ret, frame = vid_cap.read()
        if not ret:
            break
        
        # Memproses frame dan menampilkannya secara real-time
        showDetectFrame(conf, model, st_frame, frame)
    
    vid_cap.release()  # Melepaskan sumber daya setelah selesai


            
def take_picture(conf, model):
    picture = st.camera_input("Please Take a Picture")

    if picture:
        with NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
            temp_file.write(picture.read())
            temp_pict_path = temp_file.name
            
        if st.button('Detect Photo'):
            try:
                vid_cap = cv2.VideoCapture(temp_pict_path)
                st_frame = st.empty()
                while (vid_cap.isOpened()):
                    success, image = vid_cap.read()
                    if success:
                        showDetectFrame(conf,
                                        model,
                                        st_frame,
                                        image
                                       )
                    else:
                        vid_cap.release()
                        break
            except Exception as e:
                st.error("Error loading video: " + str(e))

def helpFunction():
    # Create 3 columns, with empty spaces on the left and right to center the content
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')  # Empty space to push the image to the center

    with col2:
        # Display the image in the center column
        st.image(str(settings.IMAGE_HELP))  # Adjust width as necessary

    with col3:
        st.write(' ')  # Empty space on the right

    # Project Title and Description below the image
    html_temp_about1 = """
                <div style="padding:30px; text-align:center; margin: auto;">
                    <h2>
                        Automated Real-Time Monitoring and AI Fault Detection System for Solar Panels Using Advanced Image Detection
                    </h2>
                </div>
                """
    st.markdown(html_temp_about1, unsafe_allow_html=True)

    # Divider
    st.divider()

    # Project Description
    html_temp4 = """
                <div style="padding:10px; text-align:justify;">
                    <h3>Project Description</h3>
                    This project aims to detect faulty solar panels caused by factors like physical damage, dust, animal droppings, or snow coverage. 
                    It distinguishes defective panels from those in good condition to prevent further deterioration and ensure timely maintenance. 
                    The initiative aligns with promoting sustainable and clean energy (SDGs).🌼
                </div>
                """
    st.markdown(html_temp4, unsafe_allow_html=True)


