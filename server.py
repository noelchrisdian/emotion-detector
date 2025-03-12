from flask import Flask
from EmotionDetection.emotion_detection import emotionDetector

app = Flask(__name__)

app.route('/emotionDetector')
def detect_emotion():
    