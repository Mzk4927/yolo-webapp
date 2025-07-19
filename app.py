from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
from detect_backend import detect_frame
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return "No image", 400

    file = request.files['image']
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    detected = detect_frame(frame)
    _, buffer = cv2.imencode('.jpg', detected)
    return send_file(BytesIO(buffer.tobytes()), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
