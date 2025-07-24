🧫 YOLOv11 Live Object Detection Web App
A real-time object detection web application built with YOLOv11 Nano, Flask, OpenCV, and JavaScript. This app can:
•	Perform live object detection via your browser webcam.
•	Detect objects in uploaded images.
•	Return bounding boxes with labels in real time.

🚀 Features
•	🔍 Live webcam detection
•	🖼️ Upload image for detection
•	💡 Built with YOLOv11 Nano (custom model support)
•	🌐 Flask-based web backend
•	⚡ Fast and lightweight performance (works even on mid-range laptops)
•	🎨 Simple HTML + JS front-end with live frame updates
•	✅ Supports label listing alongside annotated frame

🛠️ Tech Stack
•	Ultralytics YOLOv11
•	Python 3.10+
•	OpenCV
•	Flask
•	JavaScript
•	HTML/CSS

📁 Project Structure
yolo-webapp/
│
├── app.py                 # Flask server
├── detect_backend.py      # Detection logic using YOLO
├── script.py              # Standalone detection (image/webcam)
├── gradio_ui.py           # Gradio-based alternate UI
├── requirements.txt       # Dependencies
├── yolo11n.pt             # YOLOv11 model (custom or pretrained)
│
├── templates/
│   └── index.html         # Web UI for live detection
└── static/
    └── (optional CSS or JS)

📦 Installation
# Clone the repo
git clone https://github.com/yourusername/yolo-webapp.git
cd yolo-webapp

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt

🥪 Run the App
🔴 Start Flask Live Detection Server:
python app.py
Visit: http://localhost:5000
🖼️ Run Image/Webcam from script:
python script.py
# Choose 'image' or 'webcam' mode when prompted

📷 How It Works
•	Frontend captures webcam frames using JavaScript.
•	Frames are sent to Flask backend every 1.5 seconds.
•	Backend uses detect_backend.py to:
o	Run YOLOv11 inference
o	Annotate the frame with bounding boxes
o	Return the image + labels to frontend

✅ Sample Output
Upload Image	Live Detection
	

⚠️ Notes
•	Make sure yolo11n.pt is in the project root.
•	Your webcam must be enabled and allowed by the browser.
•	For best results, use Chrome or Firefox.

📌 TODO (Optional Improvements)

🧑‍💻 Author
Musa Tech (Zarar Khattak)
📧 [mzk4927@gmail.com]
🔗 GitHub Profile


