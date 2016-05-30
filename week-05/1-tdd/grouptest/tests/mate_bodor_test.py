import unittest
from work import anagramm, count_letters

class TestMonday(unittest.TestCase):

    def setUp(self):
        self.first_text = 'almafa'
        self.secound_text = 'famala'
        self.third_text = 'elem'

    def test_anagramm_true(self):
        self.assertTrue(anagramm(self.first_text, self.secound_text))
    def test_anagramm_false(self):
        self.assertFalse(anagramm(self.first_text, self.third_text))


if __name__ == '__main__':
    unittest.main()
