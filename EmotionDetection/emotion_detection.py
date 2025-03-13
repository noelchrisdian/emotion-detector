import requests
import json

def emotionDetector(text):
    if not text or text.strip() == '':
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {'raw_document': {'text': text}}
    
    response = requests.post(url, headers=headers, json=payload)
    response = json.loads(response.text)
    emotions = response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    return output