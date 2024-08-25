import requests

def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text using IBM Watson's Emotion Predict API.

    Parameters:
    text_to_analyse (str): The text to analyze for emotion detection.

    Returns:
    dict: The JSON response from the Watson API containing the detected emotions.

    Raises:
    ValueError: If the API request fails with a status code of 400 (Bad Request).
    Exception: If the API request fails with any other status code.
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
    
    try:
        response = requests.post(url, headers=headers, json=input_json, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 400:
            raise ValueError("Bad Request: The text input is invalid or missing.") from http_err
        else:
            raise Exception(f"HTTP error occurred: {http_err}") from http_err
    except requests.exceptions.RequestException as req_err:
        raise Exception(f"Request error occurred: {req_err}") from req_err

    return response.json()
