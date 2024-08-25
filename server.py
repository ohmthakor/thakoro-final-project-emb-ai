from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    """
    Endpoint to detect emotions in the provided text.

    Expects JSON with a 'text' field.

    Returns:
    JSON with the detected emotions or an error message.
    """
    data = request.get_json()
    
    # Check if 'text' is provided and is not empty
    if 'text' not in data or not data['text'].strip():
        return jsonify({'error': 'No text provided or text is empty'}), 400
    
    try:
        text_to_analyse = data['text']
        result = emotion_detector(text_to_analyse)
        return jsonify(result)
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    """
    Home endpoint that returns a simple message indicating that the API is running.
    """
    return "Emotion Detection API is running!"

if __name__ == "__main__":
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
