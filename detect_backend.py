# detect_backend.py

from ultralytics import YOLO
import cv2

# Load model once
model = YOLO("yolo11m.pt")

# For image upload (used later)
def detect_image(image_path):
    results = model(image_path)
    results[0].save(filename="static/output.jpg")
    return "static/output.jpg"

# For webcam frame-by-frame detection
def detect_frame(frame):
    results = model(frame)[0]
    return results.plot()


