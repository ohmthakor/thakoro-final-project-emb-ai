from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    try:
        text_to_analyse = data['text']
        result = emotion_detector(text_to_analyse)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Emotion Detection API is running!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
