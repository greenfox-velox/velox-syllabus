import unittest

from work import anagramm, count_letters

class tests(unittest.TestCase):
    def test_anagramm(self):
        self.assertTrue(anagramm('wedr', 'drew'))
        self.assertFalse(anagramm('wedr', 'dred'))
        self.assertEqual(anagramm(4, 'alma'), '')
    def test_count_letters(self):
        self.assertEqual(count_letters('def'), {'d': 1, 'e': 1, 'f': 1})
        self.assertEqual(count_letters(''), {})
        self.assertEqual(count_letters(5.03), '')

if __name__ == '__main__':
    unittest.main()
