# tests/test_emotion_detector.py

import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_happy_text(self):
        text = "I am so happy today!"
        result = emotion_detector(text)
        self.assertIn('joy', result)
        self.assertGreater(result['joy'], 0.5)

    def test_sad_text(self):
        text = "I am feeling very sad."
        result = emotion_detector(text)
        self.assertIn('sadness', result)
        self.assertGreater(result['sadness'], 0.5)

    def test_empty_text(self):
        text = ""
        with self.assertRaises(Exception):
            emotion_detector(text)

    def test_no_emotion_text(self):
        text = "The sky is blue."
        result = emotion_detector(text)
        self.assertTrue(all(score < 0.5 for score in result.values()))

if __name__ == '__main__':
    unittest.main()