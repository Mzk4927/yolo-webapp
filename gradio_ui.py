import gradio as gr
import cv2    # libraries 
from ultralytics import YOLO 


model = YOLO("yolov8n.pt") # import model 


def live_detect(frame):   # webcam 1 frame detect 
    results = model.predict(source=frame, conf=0.5, verbose=False) # prediction (yolo)
    annotated_frame = results[0].plot() #bounding boxes and labels 

    
    detected_objects = []
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        detected_objects.append(label)
    
    
    detected_list = sorted(set(detected_objects))

    
    detected_text = "Detected: " + ", ".join(detected_list) if detected_list else "No objects detected"

    return annotated_frame, detected_text


gr.Interface(
    fn=live_detect,
    inputs=gr.Image(sources=["webcam"], streaming=True),
    outputs=[gr.Image(label="Detection Frame"), gr.Textbox(label="Detected Objects")],
    live=True,
    title="YOLOv8 Live Object Detection",
    description="Real-time webcam object detection using YOLOv8 + Gradio"
).launch(share=True)