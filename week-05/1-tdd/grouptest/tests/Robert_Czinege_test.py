import unittest
from work import anagramm, count_letters


class AnagrammTestCases(unittest.TestCase):

    def setUp(self):
        self.input_string_for_letter_counter = 'aa AA Bc 11 22 ! %'
        self.expected_letter_dictionary = {'a': 4, 'b': 1, 'c': 1, '1': 2, '2': 2, '!': 1, '%': 1, ' ': 6}

    def test_are_these_strings_anagramms_of_each_other(self):
        self.assertTrue(anagramm('54AbCcD% !', 'AbCcD45! %'))
        self.assertTrue(anagramm('AlmA', 'alma'), msg='The function should be not case sensitive!')
        self.assertTrue(anagramm('123', '321'), msg='The function should handle the numbers as well!')
        self.assertTrue(anagramm('!! aa ?', 'aa !! ?'), msg='The function should handle the other characters as well!')
        self.assertFalse(anagramm('alma', 'kalap'), msg='The length of the string matters! If the length is not equal, it cannot be an anagram!')
        self.assertFalse(anagramm('Alma', 'Kalap'))
        self.assertFalse(anagramm('alma123', 'alma456'))

    def test_how_many_different_characters_are_in_this_string(self):
        self.assertEqual(count_letters(self.input_string_for_letter_counter), self.expected_letter_dictionary)


if __name__ == '__main__':
    unittest.main()
