from ultralytics import YOLO
import cv2

# Load your custom YOLOv11 model
model = YOLO("yolo11n.pt")  # Updated model path

# --- Detection on Image ---
def detect_image(image_path):
    results = model(image_path, show=True)
    results[0].save(filename="output.jpg")
    print("✅ Image detection done. Saved as output.jpg")

# --- Live Webcam Detection ---
def detect_webcam():
    cap = cv2.VideoCapture(0)  # 0 = default webcam

    if not cap.isOpened():
        print("❌ Error: Could not open webcam.")
        return

    print("📷 Press 'q' to stop webcam detection.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break

        # Resize (optional for speed boost)
        resized = cv2.resize(frame, (640, 480))

        # Run detection
        results = model(resized)[0]

        # Draw bounding boxes
        annotated_frame = results.plot()

        # Show the frame
        cv2.imshow("YOLOv11 Live", annotated_frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("🛑 Webcam detection stopped.")

# --- Main Entry Point ---
if __name__ == "__main__":
    mode = input("Choose mode (image / webcam): ").strip().lower()

    if mode == "image":
        path = input("Enter image path: ").strip()
        detect_image(path)
    elif mode == "webcam":
        detect_webcam()
    else:
        print("❌ Invalid mode. Please choose 'image' or 'webcam'.")
