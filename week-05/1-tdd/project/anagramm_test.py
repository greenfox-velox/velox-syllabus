import unittest
from anagramm import is_anagramm

class Test_is_anagramm(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(is_anagramm('', ''), True)

    def test_different(self):
        self.assertEqual(is_anagramm('a', ''), False)

    def test_reverse(self):
        self.assertEqual(is_anagramm('ab', 'ba'), True)

    def test_anagramm(self):
        self.assertEqual(is_anagramm('abc', 'bac'), True)
        self.assertEqual(is_anagramm('abcdefghij', 'jacigbhdfe'), True)

unittest.main()
