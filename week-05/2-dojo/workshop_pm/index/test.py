import unittest
from index import index

class TestIndex(unittest.TestCase):
  def test_empty(self):
    self.assertEqual(index([], 1), -1)

  def test_first_value_is_same(self):
    self.assertEqual(index([1], 1), 0)

  def test_first_value_differs(self):
    self.assertEqual(index([1], 2), -1)

  def test_second_value(self):
    self.assertEqual(index([1, 2], 2), 1)

  def test_third_value(self):
    self.assertEqual(index([1, 2, 3], 3), 2)



if __name__ == '__main__':
  unittest.main()
