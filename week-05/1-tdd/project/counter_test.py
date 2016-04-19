import unittest
from counter import count_letters

class LetterCounterTest(unittest.TestCase):
    def test_if_exists(self):
        self.assertEqual(count_letters(''), {})

    def test_same_letters(self):
        self.assertEqual(count_letters('a'), {'a': 1})
        self.assertEqual(count_letters('aa'), {'a': 2})

    def test_different_letters(self):
        self.assertEqual(count_letters('b'), {'b': 1})

    def test_distinct_letters(self):
        self.assertEqual(count_letters('ab'), {'a': 1, 'b': 1})



unittest.main()
