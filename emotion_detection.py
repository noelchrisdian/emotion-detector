import requests

def emotionDetector(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {'raw_document': {'text': text}}
    
    response = requests.post(url, headers=headers, json=payload)
    return response.text