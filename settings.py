from pathlib import Path
import sys
from streamlit_webrtc import RTCConfiguration, ClientSettings

# Mendapatkan path default
FILE = Path(__file__).resolve()
# Mengambil direktori utama
ROOT = FILE.parent
#  Menambahkan jalur root ke daftar sys.path jika belum ada
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Mendapatkan relativ path dari direktori
ROOT = ROOT.relative_to(Path.cwd())

# Mode
HOME = 'Homepage'
HOWTOUSE = 'How To Use'
IMAGE = 'Image Detection'
VIDEO = 'Video Detection'
WEBCAM = 'Real-Time Detection'

SOURCES_LIST = [HOME, HOWTOUSE, IMAGE, VIDEO, WEBCAM]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'detect.jpeg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'hasil_deteksi.jpg'
IMAGE_HELP = IMAGES_DIR / 'Tim 6_logo.png'

# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {
    'Video 1': VIDEO_DIR / 'video_1.mp4',
    'Video 2': VIDEO_DIR / 'video_2.mov',
    'Video 3': VIDEO_DIR / 'video_3.mp4',
}

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'

# Webcam source
WEBCAM_PATH = 0

# konfigurasi live-cam
WEBRTC_CLIENT_SETTINGS = ClientSettings(
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False},
    )
# List clasname
CLASS_NAME = {
    0: "Bird Drop", 
    1: "Defective",
    2: "Dust", 
    3: "Non Defective",
    4: "Physical Damage", 
    5: "Snow"
            }