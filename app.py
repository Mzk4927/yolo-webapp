from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from detect_backend import detect_frame
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['image']
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    annotated, labels = detect_frame(frame)

    _, buffer = cv2.imencode('.jpg', annotated)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')

    return jsonify({
        "image": jpg_as_text,
        "labels": labels
    })

if __name__ == '__main__':
    app.run(debug=True)
