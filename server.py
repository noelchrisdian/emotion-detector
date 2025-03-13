from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotionDetector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    text = request.args.get('text')

    result = emotionDetector(text)

    if result["dominant_emotion"] is None:
        return {"message": "Invalid text! Please try again!"}, 400

    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)