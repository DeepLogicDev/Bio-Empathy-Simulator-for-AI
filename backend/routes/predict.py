from flask import Blueprint, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import base64

predict_bp = Blueprint('predict', __name__)
model = load_model('models/emotion_model.h5')
classes = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json['image']
    img_bytes = base64.b64decode(data.split(',')[1])
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (48, 48))
    img = img.reshape(1, 48, 48, 1) / 255.0
    prediction = model.predict(img)
    emotion = classes[np.argmax(prediction)]
    return jsonify({'emotion': emotion})
