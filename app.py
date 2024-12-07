# Python In-built packages
from pathlib import Path
import PIL
import base64

# External packages
import streamlit as st

# Local Modules
import settings
import helper


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

# Pilihan deteksi
selected_option = st.sidebar.selectbox('', settings.SOURCES_LIST)

# Main page heading with extra margin
st.markdown("<h1 style='text-align: center;'>☀️Solar Panel Fault Detection🛰️</h1>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)  # Adds extra space between selectbox and title

# Sidebar About
st.sidebar.markdown("# About Us")
st.sidebar.image("images/brainstorm.png", use_column_width=True, width=400)  # Resize the image to be larger
st.sidebar.divider()

# Data untuk anggota tim
team_members = [
    {
        "role": "Team Leader",
        "name": "Jamilatul Muyasaroh",
        "linkedin": "https://id.linkedin.com/in/jamilatul-muyasaroh-1071ba300",
        "instagram": "https://www.instagram.com/miilaaaj",
        "photo": "images/Jamilatul Muyasaroh_UNS.PNG"
    },
    {
        "role": "Team Member",
        "name": "Elvizto Juan Khresnanda",
        "linkedin": "www.linkedin.com/in/elviztookhresnanda",
        "instagram": "https://www.instagram.com/juonelviztoo/",
        "photo": "images/elvizto.jpg"
    },
    {
        "role": "Team Member",
        "name": "Bimo Prawiradijaya",
        "linkedin": "https://linkedin.com/in/bimopd",
        "instagram": "https://www.instagram.com/bimoprawiradjaya",
        "photo": "images/bimoprawira.jpg"
    },
    {
        "role": "Team Member",
        "name": "M. Bagas Abidawaqli",
        "linkedin": "https://www.linkedin.com/in/m-bagas-abidawaqli-5985a320a/",
        "instagram": "https://www.instagram.com/mbadawaqli484",
        "photo": "images/M.BagasAbidawaqli_UNS.png"
    },
    {
        "role": "Team Member",
        "name": "Yoga Yudha Tama",
        "linkedin": "https://www.linkedin.com/in/yoga-yudha-tama/",
        "instagram": "https://www.instagram.com/yogaacor_/",
        "photo": "images/Yoga Yudha Tama_UNNES.png"
    },
    {
        "role": "Team Member",
        "name": "Yudanis Dwi Satria",
        "linkedin": "https://www.linkedin.com/in/yudanis-dwi-satria-142a61229/",
        "instagram": "https://www.instagram.com/danissaatria/",
        "photo": "images/Yudanis.jpg"
    },
    {
        "role": "Team Member",
        "name": "Laras Wati",
        "linkedin": "https://www.linkedin.com/in/laras-wati-934b58251/",
        "instagram": "https://www.instagram.com/laras444",
        "photo": "images/Laras.jpg"
    },
]

# Info Anggota
for member in team_members:
    st.sidebar.markdown(f"### {member['name']}")
    st.sidebar.markdown(f"**{member['role']}**")
    st.sidebar.markdown(f"[LinkedIn]({member['linkedin']})" "  " f"[Instagram]({member['instagram']})")
    st.sidebar.image(member['photo'], use_column_width=True)
    st.sidebar.divider()

source_img = None

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
