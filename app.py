# Python In-built packages
from pathlib import Path
import PIL
import base64

# External packages
import streamlit as st

# Local Modules
import settings
import helper

# Setting page layout
# st.set_page_config(
#     page_title="Deteksi Objek | Yolov8",
#     page_icon="🔍",
# )

# def set_background(image_path):
#     """
#     Fungsi untuk mengatur background dengan gambar lokal.
#     :param image_path: Path ke gambar lokal
#     """
#     # Encode gambar sebagai Base64
#     with open(image_path, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()
#     # Tambahkan ke CSS
#     st.markdown(f"""
#         <style>
#         body {{
#             background-image: url("data:image/jpeg;base64,{encoded_string}");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#             background-position: center;
#             background-color: #f0f0f0; /* Warna fallback */
#         }}
#         </style>
#         """, unsafe_allow_html=True)

# # Set Background
# set_background("assets/PanelBG-1.jpg")

# settings
model_type = 'Detection'
confidence = 0.4
model_path = Path(settings.DETECTION_MODEL)

# Load Model
try:    
    model = helper.load_model(model_path)
except Exception as ex:
    print(f"Unable to load model. Check the specified path: {model_path}")
    print(ex)

# Main page heading
st.markdown("<h1 style='text-align: center;'>☀️Solar Panel Fault Detection🛰️</h1>", unsafe_allow_html=True)

# Pilihan deteksi
selected_option = st.selectbox('Silahkan Pilih Mode Deteksi:', settings.SOURCES_LIST)

source_img = None

# pilihan selectbox

# jika yang dipilih image
# Petunjuk
if selected_option == settings.HOME:
    helper.helpFunction()
    
elif selected_option == settings.IMAGE:
    tab1, tab2 = st.tabs(["Upload", "Buka Kamera"])
    with tab1:
        # Slider untuk mengatur confidence
        confidence = st.slider("Atur Confidence Level:", min_value=0.0, max_value=1.0, value=0.4, step=0.05)
        source_img = st.file_uploader(
            "Silahkan Mengupload Gambar", type=("jpg", "jpeg", "png"))
        
        col1, col2 = st.columns(2)
        res_plotted = None
        with col1:
            try:
                if source_img is None:
                    default_image_path = str(settings.DEFAULT_IMAGE)
                    default_image = PIL.Image.open(default_image_path)
                    st.image(default_image_path, caption="Gambar Awal",
                            use_column_width=True)
                else:
                    uploaded_image = PIL.Image.open(source_img)
                    st.image(source_img, caption="Gambar Awal",
                            use_column_width=True)
                    
                    # Tombol Detect Objects di sini
                    if st.button('Deteksi'):
                        res = model.predict(uploaded_image, conf=confidence)
                        boxes = res[0].boxes
                        res_plotted = res[0].plot()[:, :, ::-1]

            except Exception as ex:
                st.error("Ada Kesalahan Saat Membaca File")
                st.error(ex)

        with col2:
            if source_img is None:
                default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
                default_detected_image = PIL.Image.open(
                    default_detected_image_path)
                st.image(default_detected_image_path, caption='Gambar Hasil Deteksi',
                        use_column_width=True)
            else:
                if res_plotted is not None:
                    st.image(res_plotted, caption='Gambar Hasil Deteksi')
                    
                    class_indices = set(boxes.cls.tolist())
                    unique_labels = [settings.CLASS_NAME[idx] for idx in class_indices]

                    with st.expander("Hasil Deteksi"):
                        if unique_labels:
                            st.success(', '.join(unique_labels))
                        else:
                            st.warning("Tidak Ada Objek Yang Terdeteksi")
                else:
                    st.empty()
    with tab2:
        # Slider untuk mengatur confidence
        confidence = st.slider("Atur Confidence Level (Kamera):", min_value=0.0, max_value=1.0, value=0.4, step=0.05)
        helper.take_picture(confidence, model)

# Jika pilihan video
elif selected_option == settings.VIDEO:
    tab1, tab2 = st.tabs(["Upload", "Sumber Asal"])
    with tab1:
        # Slider untuk mengatur confidence
        confidence = st.slider(
            "Atur Confidence Level (Video):", 
            min_value=0.0, 
            max_value=1.0, 
            value=st.session_state.get("video_confidence", 0.4), 
            step=0.05,
            key="video_confidence"
        )
        # Confidence langsung dipakai di fungsi helper
        helper.process_uploaded_video(st.session_state.video_confidence, model)

    with tab2:
        # Slider untuk mengatur confidence
        confidence = st.slider(
            "Atur Confidence Level (Sumber Asal):", 
            min_value=0.0, 
            max_value=1.0, 
            value=st.session_state.get("source_confidence", 0.4), 
            step=0.05,
            key="source_confidence"
        )
        # Confidence langsung dipakai di fungsi helper
        helper.play_stored_video(st.session_state.source_confidence, model)

# Jika pilihan youtube
elif selected_option == settings.YOUTUBE:
    # Slider untuk mengatur confidence
    confidence = st.slider(
        "Atur Confidence Level (YouTube):", 
        min_value=0.0, 
        max_value=1.0, 
        value=st.session_state.get("youtube_confidence", 0.4), 
        step=0.05,
        key="youtube_confidence"
    )
    # Confidence langsung dipakai di fungsi helper
    helper.play_youtube(st.session_state.youtube_confidence, model)

# Jika pilihan realtime / webcam
elif selected_option == settings.WEBCAM:
    # Slider untuk mengatur confidence
    confidence = st.slider(
        "Atur Confidence Level (Real-time):", 
        min_value=0.0, 
        max_value=1.0, 
        value=st.session_state.get("webcam_confidence", 0.4), 
        step=0.05,
        key="webcam_confidence"
    )
    # Confidence langsung dipakai di fungsi helper
    helper.live(st.session_state.webcam_confidence, model)