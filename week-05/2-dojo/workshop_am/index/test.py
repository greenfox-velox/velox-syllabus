import unittest
from index import index

class IndexTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(index([], 1), -1)

    def test_first_value_is_same(self):
        self.assertEqual(index([1], 1), 0)

    def test_first_value_not_same(self):
        self.assertEqual(index([2], 1), -1) 
    def test_second_value_is_same(self):
        self.assertEqual(index([0, 1], 1), 1)

    def test_third_value_is_same(self):
        self.assertEqual(index([0, 1, 2], 2), 2)

if __name__ == '__main__':
    unittest.main()

