import unittest
from work import anagramm, count_letters

class peet_test_class(unittest.TestCase):
    def setUp(self):
        pass

    def test_anagram_result_true(self):
        self.assertTrue( anagramm('alla', 'lala'))

    def test_anagram_uppercase(self):
        self.assertTrue( anagramm('MOTTO', 'TomOT'))

    def test_anagram_input_string_1_wrong_type(self):
        self.assertFalse( anagramm('st4g5', 'dfase'))

    def test_anagram_input_string_2_wrong_type(self):
        self.assertFalse( anagramm('ello', '0lle'))

    def test_anagram_whitespace(self):
        self.assertFalse( anagramm('get up', 'puteg'))

	def test_letter_count_wrong_type(self):
		self.assertFalse(count_letters(34678))

if __name__ == '__main__':
    unittest.main()
