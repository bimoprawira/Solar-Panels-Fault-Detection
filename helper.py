from ultralytics import YOLO
import time
import streamlit as st
import cv2
from pytube import YouTube
from tempfile import NamedTemporaryFile

from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, WebRtcMode, VideoProcessorFactory
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

import settings
import turn

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

def load_model(model_path):
    model = YOLO(model_path)
    return model


def showDetectFrame(conf, model, st_frame, image, is_display_tracking=None, tracker=None):

    # Predict the objects in the image using the YOLOv8 model
    res = model.predict(image, conf=conf)

    # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   )

def play_youtube(conf, model):
    
    source_youtube = st.text_input("Silahkan Masukan Link YouTube")

    if st.button('Deteksi'):
        try:
            yt = YouTube(source_youtube)
            stream = yt.streams.filter(file_extension="mp4", res=720).first()
            vid_cap = cv2.VideoCapture(stream.url)

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
            st.error("Ada Kesalahan Saat Memproses Link: " + str(e))


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
        
    st.write("Webcam mode started.")

def check_camera_source(source=0):
    vid_cap = cv2.VideoCapture(source)
    if not vid_cap.isOpened():
        raise ValueError(f"Kamera tidak tersedia pada sumber {source}")
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
        with NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
            temp_file.write(uploaded_video.read())
            temp_video_path = temp_file.name
        
        with open(temp_video_path, 'rb') as video_file:
            video_bytes = video_file.read()
        if video_bytes:
            st.video(video_bytes)
            
        if st.button('Deteksi'):
            try:
                vid_cap = cv2.VideoCapture(temp_video_path)
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

def play_stored_video(conf, model):

    source_vid = st.selectbox(
        "Silahkan Pilih Video yang Sudah Disediakan", settings.VIDEOS_DICT.keys())

    with open(settings.VIDEOS_DICT.get(source_vid), 'rb') as video_file:
        video_bytes = video_file.read()
    if video_bytes:
        st.video(video_bytes)

    if st.button('Deteksi Video'):
        try:
            vid_cap = cv2.VideoCapture(
                str(settings.VIDEOS_DICT.get(source_vid)))
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
            st.error("Ada Kesalahan Saat Proses Video: " + str(e))
            
def take_picture(conf, model):
    picture = st.camera_input("Silahkan Mengambil Gambar")

    if picture:
        with NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
            temp_file.write(picture.read())
            temp_pict_path = temp_file.name
            
        if st.button('Deteksi Foto'):
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
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')
    with col2:
        st.image(str(settings.IMAGE_HELP))
    with col3:
        st.write(' ')
        
    html_temp_about1= """
                <div style="padding:10px; text-align:center;">
                    <h2>
                        Automated Real-Time Monitoring and AI Fault Detection System for Solar Panels Using Advanced Image Detection
                    </h2>
                </div>
                """
    st.markdown(html_temp_about1, unsafe_allow_html=True)
    st.divider()

    html_temp4 = """
                <div style="padding:10px">
                    <div>
                    <h3>Project Description</h3>
                    This project aims to detect faulty solar panels caused by factors like physical damage, dust, animal droppings, or snow coverage. It distinguishes defective panels from those in good condition to prevent further deterioration and ensure timely maintenance. 
                    The initiative aligns with promoting sustainable and clean energy (SDGs).🌼
                    </div>
                </div>

                <br>
                
                <div>
                    
                </div>
                """

    st.markdown(html_temp4, unsafe_allow_html=True)