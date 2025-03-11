import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_empty_string(self):
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])

    def test_numeric_input(self):
        result = emotion_detector("12345")
        self.assertIsNone(result['dominant_emotion'])

    def test_special_characters(self):
        result = emotion_detector("!@#$%^&*()")
        self.assertIsNone(result['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()