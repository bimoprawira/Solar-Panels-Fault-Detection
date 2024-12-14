# Python In-built packages
from pathlib import Path
import PIL
import base64

# External packages
import streamlit as st

# Local Modules
import settings
import helper
from helper import notify_solution


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

st.set_page_config(page_title="Solar Panel Fault Detection", page_icon="images/brainstorm.png")

# Pilihan deteksi
selected_option = st.sidebar.selectbox('', settings.SOURCES_LIST)

# Main page heading with extra margin
st.markdown("<h1 style='text-align: center;'>☀️Solar Panel Fault Detection🛰️</h1>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)  # Adds extra space between selectbox and title

# Sidebar About
st.sidebar.markdown("# About Us")
st.sidebar.image("images/brainstorm.png", use_column_width=True)  # Resize the image to be larger
# Tambahkan tautan gambar YouTube dan GitHub di sidebar
st.sidebar.markdown(
    """
    <div style="position: relative; display: flex; justify-content: center; align-items: center;">
        <a href="https://youtu.be/vZlyn8Qw2o4?si=3lupeZHI5D37prC5" target="_blank">
            <img src="https://badges.aleen42.com/src/youtube.svg" alt="YouTube"style="margin-right: 10px">
        </a>
        <a href="https://github.com/6rainstorm/Solar-Panels-Fault-Detection" target="_blank">
            <img src="https://badges.aleen42.com/src/github.svg" alt="GitHub">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
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
linkedin_logo = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg"
instagram_logo = "https://download.logo.wine/logo/Instagram/Instagram-Logo.wine.png"

for member in team_members:
    st.sidebar.markdown(f"### {member['name']}")
    st.sidebar.markdown(f"**{member['role']}**")
    st.sidebar.image(member['photo'], use_container_width=True)
    st.sidebar.markdown(
        f"""
        <div style="position: relative; display: flex; justify-content: center; align-items: center; margin-bottom:0">
            <a href="{member['linkedin']}" target="_blank">
                <img src="{linkedin_logo}" alt="LinkedIn" style="width: 60px;margin-right: 8px;">
            </a>
            <a href="{member['instagram']}" target="_blank">
                <img src="{instagram_logo}" alt="Instagram" style="width: 50px; ">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.divider()

source_img = None

# Petunjuk
if selected_option == settings.HOME:
    helper.helpFunction()

elif selected_option == settings.HOWTOUSE:
    st.markdown("""
    ### How to Use the Program ⚠️
    
    - **Navigate to Desired Feature**  
      Use the navigation menu on **sidebar** of the screen to select the feature you want to use:
      - **Image Detection**
      - **Video Detection**
      - **Real-Time Detection**

    - **Image Detection**   
      - To upload an image, click **"Upload"** and select a file from your device. Supported formats include JPG, JPEG, and PNG.  
      - Alternatively, click **"Open Camera"** to capture an image directly.  
      - Adjust the **confidence level slider** to set the desired accuracy for detection.  
      - The program will analyze the image and display the detection results with labels and suggested solutions.

    - **Video Detection**  
      - Upload a video by clicking **"Upload"**. Supported formats include MP4, AVI, MOV, and MPEG4.  
      - Adjust the **confidence level slider** to modify detection sensitivity.  
      - The program will process the video and display the results

    - **Real-Time Detection**  
      - Choose a camera device for live detection by clicking **"Select Device"**.  
      - Adjust the **confidence level slider** to set the detection accuracy.  
      - Click **"Start"** to begin real-time detection. The program will show live detection results with labels on the screen.

    ### Tips for Optimal Use 💡
    - Ensure uploaded images or videos are clear and focused to improve detection accuracy.
    - When using the real-time detection feature, ensure the camera is positioned steadily, and the solar panels are fully visible.
    - Adjust the confidence level appropriately—higher values may reduce false positives, but lower values may help detect minor defects.
    - For video detection, make sure the panels are in motion or clearly visible to ensure accurate processing.
    - Avoid using extremely low-quality images or videos, as this can lead to inaccurate results.
    """, unsafe_allow_html=True)


elif selected_option == settings.IMAGE:
    tab1, tab2 = st.tabs(["Upload", "Open Camera"])
    with tab1:
        # Slider untuk mengatur confidence
        confidence = st.slider("Set Confidence Level:", min_value=0.0, max_value=1.0, value=0.4, step=0.05)
        source_img = st.file_uploader(
            "Please Upload an Image", type=("jpg", "jpeg", "png"))
        
        col1, col2 = st.columns(2)
        res_plotted = None
        with col1:
            try:
                if source_img is None:
                    default_image_path = str(settings.DEFAULT_IMAGE)
                    default_image = PIL.Image.open(default_image_path)
                    st.image(default_image_path, caption="Original Image",
                            use_container_width=True)
                else:
                    uploaded_image = PIL.Image.open(source_img)
                    st.image(source_img, caption="Original Image",
                            use_container_width=True)
                    
                    # Tombol Detect Objects di sini
                    if st.button('Detection'):
                        res = model.predict(uploaded_image, conf=confidence)
                        boxes = res[0].boxes
                        res_plotted = res[0].plot()[:, :, ::-1]

            except Exception as ex:
                st.error("An Error Occurred While Reading the File")
                st.error(ex)

        with col2:
            if source_img is None:
                default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
                default_detected_image = PIL.Image.open(default_detected_image_path)
                st.image(default_detected_image_path, caption='Detection Result Image', use_container_width=True)
            else:
                if res_plotted is not None:
                    st.image(res_plotted, caption='Detection Result Image')

                    # Get detected labels
                    class_indices = set(boxes.cls.tolist())  # Get class indices from detection results
                    unique_labels = [settings.CLASS_NAME[idx] for idx in class_indices]  # Convert indices to labels

                    # Display detected labels in an expander
                    with st.expander("Detected Labels"):
                            if unique_labels:
                                label_colors = {
                                    "Snow": "background-color:rgba(65, 201, 226, 0.85);color:white;",  
                                    "Dust": "background-color:rgba(166, 110, 56);color:white;",  # Oranye
                                    "Bird Drop": "background-color:rgba(165, 157, 132);color:white;",  # Merah Tua
                                    "Physical Damage": "background-color:rgba(16, 44, 87);color:white;",  # Merah
                                    "Defective": "background-color:rgba(159,0,0,255);color:white;",  # Merah Gelap
                                    "Non Defective": "background-color:rgba(50, 205, 50, 0.5);color:white;",  # Hijau
                                }

                                # Generate HTML labels
                                labels_html = ""
                                for label in unique_labels:
                                    color_style = label_colors.get(label, "background-color:#D3D3D3;color:black;")  # Default abu-abu
                                    labels_html += f"""
                                    <span style="{color_style};padding:10px 10px; border-radius:5px; margin-right:5px; margin-bottom:10px; display:inline-block;">
                                        {label}
                                    </span>
                                    """

                                # Render labels as HTML
                                st.markdown(
                                    f"""
                                    <div style="margin-top:5px;">
                                        {labels_html}
                                    </div>
                                    """,
                                    unsafe_allow_html=True
                                )
                            else:
                                st.warning("No objects detected.")

                    
                    # Display solution notifications below detected labels with padding
                    st.markdown("## Solutions:")
                    for label in unique_labels:
                        if label in settings.CLASS_NAME.values():
                            message, color = {
                                "Snow": ("The panels are indicated as being covered with snow, please clear it as soon as possible!", "rgba(65, 201, 226, 0.85)"),  
                                "Dust": ("The panels are indicated as being covered with dust or dirt, please clean it as soon as possible!", "rgba(166, 110, 56, 0.9)"),  
                                "Bird Drop": ("The panels are indicated with bird droppings, please clean it up as soon as possible!", "rgba(165, 157, 132)"),  
                                "Physical Damage": ("The panels are indicated to have physical damage! It's mandatory to replace the panel if it's indicated to be defective as well. Otherwise, the panel can still be used, just less optimally and efficiently.", "rgba(16, 44, 87)"),  
                                "Defective": ("The panels are indicated to be defective or malfunctioning! Take immediate action or replace it to avoid further deterioration (depending on what detection is found).", "rgba(159,0,0,255)"), 
                                "Non Defective": ("The panels are indicated to be in good and healthy condition! Please keep the solar panels in a stable condition for the future.", "rgba(50, 205, 50, 0.5)"),  
                            }[label]
                            st.markdown(
                                f"""
                                <div style="background-color:{color};padding:15px;margin-bottom:10px;border-radius:5px;">
                                    <b>{message}</b>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

    with tab2:
        # Slider untuk mengatur confidence
        confidence = st.slider("Adjust Confidence Level (Camera):", min_value=0.0, max_value=1.0, value=0.4, step=0.05)
        helper.take_picture(confidence, model)

# Jika pilihan video
elif selected_option == settings.VIDEO:
    tab1, tab2 = st.tabs(["Upload", "Original Source"])
    with tab1:
        # Slider untuk mengatur confidence
        confidence = st.slider(
            "Set Confidence Level (Video):", 
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
            "Set Confidence Level (Original Source):", 
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
        "Set Confidence Level (Real-time):", 
        min_value=0.0, 
        max_value=1.0, 
        value=st.session_state.get("webcam_confidence", 0.4), 
        step=0.05,
        key="webcam_confidence"
    )
    # Confidence langsung dipakai di fungsi helper
    helper.live(st.session_state.webcam_confidence, model)
