import unittest
from work import anagramm
from work import count_letters

class AnagramTest(unittest.TestCase):
    def test_for_case_sensitivity(self):
        self.assertTrue(anagramm("alma","aLmA"))
    def test_for_complication(self):
        self.assertFalse(anagramm("skfjhKUI&tgfkjh","sidkjfhb4k"))
    def test_for_similar_parameters(self):
        self.assertFalse(anagramm("akksi","akksik"))
    def test_for_sepcial_characters(self):
        self.assertTrue(anagramm("&%^?!.,", ",?&!%^."))

class CountLettersTest(unittest.TestCase):
    def test_for_case_sensitivity(self):
        self.assertEqual(count_letters("Attila"), {'a': 2, 't': 2, 'i': 1, 'l': 1})
    def test_for_lorem_ipsum(self):
        self.assertEqual(count_letters("Lorem ipsum dolor sit amet, massa in pede augue, pariatur lectus lectus nostra et nonummy felis, ut justo donec, volutpat vitae donec pharetra."), {'j': 1, '.': 1, 'i': 6, 'l': 6, 'a': 11, 't': 13, 'f': 1, 'o': 9, 'n': 6, 'v': 2, 'r': 7, 'u': 10, 'e': 13, 's': 9, 'c': 4, 'g': 1, ' ': 22, 'y': 1, 'p': 5, ',': 4, 'm': 6, 'h': 1, 'd': 4})

if __name__ == '__main__':
    unittest.main()
