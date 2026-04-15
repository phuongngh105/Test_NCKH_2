import cv2
import os

# ================= CONFIG =================
video_paths = [
    r"C:\Users\Hp\Downloads\video source\video1.mp4",
    r"C:\Users\Hp\Downloads\video source\video2.mp4",
    r"C:\Users\Hp\Downloads\video source\video3.mp4",
    r"C:\Users\Hp\Downloads\video source\video4.mp4"
]

output_path = "output_merged.mp4"
TARGET_FPS = 25
TARGET_SIZE = (640, 480)  # (width, height)
# ==========================================


def get_video_duration(cap):
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    return frames / fps


# Load all videos
caps = [cv2.VideoCapture(p) for p in video_paths]

# Check all opened
for i, cap in enumerate(caps):
    if not cap.isOpened():
        raise Exception(f"Cannot open video {video_paths[i]}")

# Find shortest duration
min_duration = min(get_video_duration(cap) for cap in caps)
max_frames = int(min_duration * TARGET_FPS)

print(f"Min duration: {min_duration:.2f}s -> {max_frames} frames")

# Prepare writer (2x2 grid)
out_width = TARGET_SIZE[0] * 2
out_height = TARGET_SIZE[1] * 2

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, TARGET_FPS, (out_width, out_height))

# Read and process
frame_count = 0

while frame_count < max_frames:
    frames = []

    for cap in caps:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize
        frame = cv2.resize(frame, TARGET_SIZE)
        frames.append(frame)

    if len(frames) < 4:
        break

    # Merge 2x2
    top = cv2.hconcat([frames[0], frames[1]])
    bottom = cv2.hconcat([frames[2], frames[3]])
    merged = cv2.vconcat([top, bottom])

    out.write(merged)
    frame_count += 1

# Release
for cap in caps:
    cap.release()

out.release()

print("Done! Saved to", output_path)


# ================= NOTE =================
# Install:
# pip install opencv-python
#
# Run:
# python your_script.py
# ======================================
