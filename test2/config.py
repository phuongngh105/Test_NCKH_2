'''
project/
│
├── main.py
├── config.py
├── roi_config.py
├── sumo_config/
│   └── your_simulation.sumocfg
├── video.mp4   (hoặc dùng camera)
'''

MODEL_PATH = r"D:\TRaining Data\test2\yolov8s_model.pt"   # hoặc yolov26s.pt của bạn
VIDEO_INPUT = r"D:\TRaining Data\test2\video.mp4"   # hoặc 0 nếu dùng webcam
SUMO_CFG =  r"D:\TRaining Data\test2\sumo_config\run1.sumocfg"

CONF = 0.3

CLASS_NAMES = ['car']

# mapping ROI → edge trong SUMO
ROI_TO_EDGE = {
    "Zone_A": "W2C",
    "Zone_B": "N2C",
    "Zone_C": "E2C",
}