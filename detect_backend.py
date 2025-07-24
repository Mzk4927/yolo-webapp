# detect_backend.py
from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt")  # Make sure this file exists

def detect_frame(img):
    results = model.predict(source=img, conf=0.5, verbose=False)
    annotated = results[0].plot()
    
    # Extract detected labels
    labels = []
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        labels.append(label)

    return annotated, labels
