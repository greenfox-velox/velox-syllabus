import unittest
from work import anagramm, count_letters

class TestExamples(unittest.TestCase):

    def test_anagramm_if_true(self):
        self.assertTrue(anagramm('alma', 'mala'))

    def test_anagramm_if_case_sensitive(self):
        self.assertTrue(anagramm('alma', 'Mala'))

    def test_anagramm_with_numbers(self):
        self.assertFalse(anagramm(1234, 3421))

    def test_anagramm_with_numbers(self):
        self.assertTrue(count_letters('alma'), {'l': 1, 'a': 2, 'm': 1})

    def test_anagramm_with_numbers(self):
        self.assertFalse(count_letters(1234))

if __name__ == '__main__':
    unittest.main()
