import unittest
from work import anagramm
from work import count_letters

class TestCase(unittest.TestCase):

    def test_anagramm_same_characters(self):
        self.assertTrue(anagramm('alma', 'lama'))

    def test_anagramm_same_characters_with_uppercase_letters(self):
        self.assertTrue(anagramm('Alma', 'lAma'))

    def test_anagramm_with_other_uppercase_letters(self):
        self.assertTrue(anagramm('Alma', 'Lama'))

    def test_anagramm_same_characters_with_spaces(self):
        self.assertTrue(anagramm('al ma', 'l ama'))

    def test_anagramm_numbers_in_string(self):
        self.assertTrue(anagramm('123', '321'))

    def test_anagramm_empty_string(self):
        self.assertFalse(anagramm('', ''))

    def test_anagramm_integers(self):
        self.assertFalse(anagramm(123, 231))

    def test_count_lowercase_letters(self):
        self.assertEqual(count_letters('alma'), {'a':2, 'l':1, 'm':1})

    def test_count_lower_and_uppercase_letters(self):
        self.assertEqual(count_letters('Alma'), {'a':2, 'l':1, 'm':1})

    def test_count_numbers_in_string(self):
        self.assertEqual(count_letters('11233'), {'1':2, '2':1, '3':2})

    def test_count_letters_with_spaces(self):
        self.assertEqual(count_letters('a l m a'), {'a':2, 'l':1, 'm':1, ' ':3})

    def test_count_empty_string(self):
        self.assertEqual(count_letters(''), {})

    def test_count_integers(self):
        self.assertEqual(count_letters(11233), {'1':2, '2':1, '3':2})


if __name__ == '__main__':
    unittest.main()
