import requests

def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text using IBM Watson's Emotion Predict API.

    Parameters:
    text_to_analyse (str): The text to analyze for emotion detection.

    Returns:
    dict: The JSON response from the Watson API containing the detected emotions.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

# Example usage:
if __name__ == "__main__":
    text = "I am so happy today!"
    result = emotion_detector(text)
    print(result)
