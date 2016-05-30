import unittest
from work import anagramm
from work import count_letters


class AnagrammTestCase(unittest.TestCase):

    def test_anagramm_is_true(self):
        self.assertTrue(anagramm('alma', 'mala'))

    def test_anagramm_is_false(self):
        self.assertFalse(anagramm('alma', 'lamm'))

    def test_number_anagramm_is_True(self):
        self.assertTrue(anagramm('-1548', '1584-'))

    def test_letter_counter_True(self):
        self.assertEqual(count_letters('alma'), count_letters('mala'))

    def test_letter_counter_notequal(self):
        self.assertNotEqual(count_letters('alma'), count_letters('kkkkddddd'))

    def test_letter_counter_uppercase(self):
        self.assertNotEqual(count_letters('alMa'), count_letters('mala'))



if __name__ == '__main__':
    unittest.main()
