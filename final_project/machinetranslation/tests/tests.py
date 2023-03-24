import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french1(self):
        print("Testing assertEqual english_to_french")
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_english_to_french2(self):
        print("Testing assertNotEqual english_to_french")
        self.assertNotEqual(english_to_french('Hello'), 'Hello')


class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english1(self):
        print("Testing assertEqual french_to_english")
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_french_to_english2(self):
        print("Testing assertBNotEqual french_to_english")
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')



if __name__ == "__main__":
    unittest.main()
