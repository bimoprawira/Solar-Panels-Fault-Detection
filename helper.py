from ultralytics import YOLO
import time
import streamlit as st
import cv2
import requests
from pytube import YouTube
from tempfile import NamedTemporaryFile

from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, WebRtcMode, VideoProcessorFactory
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

import settings
import turn

import tempfile
import torch
import threading
import time

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

def load_model(model_path):
    model = YOLO(model_path)
    if torch.cuda.is_available():
        model.to('cuda')  # Memindahkan model ke GPU jika tersedia
    return model



def showDetectFrame(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    # Mengubah ukuran frame agar lebih kecil untuk deteksi yang lebih cepat
    small_image = cv2.resize(image, (640, 480))  # Mengubah resolusi menjadi 640x480
    res = model.predict(small_image, conf=conf)
    res_plotted = res[0].plot()
    st_frame.image(res_plotted, caption='Detected Video', channels="BGR")


# def play_youtube(conf, model):
#     source_youtube = st.text_input("Silahkan Masukkan Link YouTube")
    
#     if source_youtube:
#         if st.button('Deteksi'):
#             try:
#                 # Path ke file cookies yang diekspor dari browser
#                 cookies_path = "path/to/your/cookies.txt"  # Sesuaikan dengan path cookies Anda

#                 # Set up options for yt-dlp to extract the best quality video stream
#                 ydl_opts = {
#                     'format': 'best[ext=mp4]',
#                     'noplaylist': True,  # Ignore playlists
#                     'outtmpl': tempfile.mktemp(suffix='.mp4'),  # Temporary file output
#                     'cookies': cookies_path,  # Menambahkan opsi cookies
#                 }

#                 with ydl.YoutubeDL(ydl_opts) as ydl_instance:
#                     info_dict = ydl_instance.extract_info(source_youtube, download=False)
#                     video_url = info_dict['url']

#                     # Unduh video dan simpan sementara
#                     temp_video = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
#                     temp_video.close()

#                     # Mengunduh file video
#                     ydl_instance.download([source_youtube])

#                     # Baca video menggunakan OpenCV
#                     vid_cap = cv2.VideoCapture(temp_video.name)
#                     st_frame = st.empty()

#                     while vid_cap.isOpened():
#                         success, image = vid_cap.read()
#                         if success:
#                             # Deteksi objek di setiap frame
#                             showDetectFrame(conf, model, st_frame, image)
#                         else:
#                             vid_cap.release()
#                             break

#             except Exception as e:
#                 st.error(f"Terjadi kesalahan saat memproses video: {str(e)}")


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
    source_vid = st.selectbox("Silahkan Pilih Video yang Sudah Disediakan", settings.VIDEOS_DICT.keys())
    video_path = settings.VIDEOS_DICT.get(source_vid)
    
    if video_path is None:
        st.error("Video tidak ditemukan.")
        return
    
    vid_cap = cv2.VideoCapture(str(video_path))
    if not vid_cap.isOpened():
        st.error(f"Tidak dapat membuka video: {video_path}")
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
                <div style="padding:50px; text-align:center;">
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
                <div style="padding:10px; text-align:center;">
                    <h3>Project Description</h3>
                    This project aims to detect faulty solar panels caused by factors like physical damage, dust, animal droppings, or snow coverage. 
                    It distinguishes defective panels from those in good condition to prevent further deterioration and ensure timely maintenance. 
                    The initiative aligns with promoting sustainable and clean energy (SDGs).🌼
                </div>
                """
    st.markdown(html_temp4, unsafe_allow_html=True)


