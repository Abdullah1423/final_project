# EmotionDetection/emotion_detection.py
import requests
import json
import string

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    if not text_to_analyse or text_to_analyse.isdigit() or all(c in string.punctuation for c in text_to_analyse):
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    try:
        response = requests.post(url, json=myobj, headers=header)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        formatted_response = response.json()

        if 'emotionPredictions' not in formatted_response or not formatted_response['emotionPredictions']:
            return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

        anger = emotion_scores.get('anger', None)
        disgust = emotion_scores.get('disgust', None)
        fear = emotion_scores.get('fear', None)
        joy = emotion_scores.get('joy', None)
        sadness = emotion_scores.get('sadness', None)

        emotions = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}

        if all(value is None for value in emotions.values()):
            return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

    except requests.exceptions.RequestException as e:
        if response.status_code == 400:
            return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
        else:
            return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    except (json.JSONDecodeError, KeyError) as e:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    except Exception as e:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}