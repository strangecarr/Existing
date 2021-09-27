
import unittest

from translator import english_to_french, french_to_english

class Test_english_to_french(unittest.TestCase):

    def test1(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("Hello"),"Hello")

    def test2(self):
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("Bonjour"),"Bonjour")



if __name__ == "__main__":

    unittest.main()