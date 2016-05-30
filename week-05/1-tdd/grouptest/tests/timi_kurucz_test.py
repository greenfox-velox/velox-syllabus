import unittest
from work import anagramm, count_letters

class WordsTestCase(unittest.TestCase):
    def test_different_lowercase_words_not_anagrams(self):
        self.assertFalse(anagramm('hello', 'ehollka'))
    def test_words_uppercase_letter_are_anagrams(self):
        self.assertTrue(anagramm('aLma', 'Alma'))
    def test_empty_strings_not_anagrams(self):
        self.assertFalse(anagramm('', ''))

    def test_same_word_in_different_order(self):
        self.assertEqual(count_letters('hello'), count_letters('olleh'))
    def test_uppercase_letter_in_string(self):
        self.assertEqual(count_letters('helLo'), count_letters('olleh'))
    def test_different_words_not_equal(self):
        self.assertNotEqual(count_letters('hello'), count_letters('fkjdkllsi'))
    def test_empty_string(self):
        self.assertEqual(count_letters(''), {})




if __name__ == '__main__':
    unittest.main()
