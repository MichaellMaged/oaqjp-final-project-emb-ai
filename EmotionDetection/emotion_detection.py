import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotion_name = list(formatted_response['emotionPredictions'][0]['emotion'].keys())
    score=list(formatted_response['emotionPredictions'][0]['emotion'].values())
    emotion_response=dict(zip(emotion_name,score))
    dominant_emotion=max(emotion_response, key=lambda key: emotion_response[key])
    emotion_response.update({'Dominant emotion':dominant_emotion})
    return emotion_response
    