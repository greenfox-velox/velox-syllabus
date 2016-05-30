import unittest
from work import anagramm, count_letters


class test_my_work(unittest.TestCase):
  def setUp(self):
    self.dictionary = {'c':1, 'a':1, 't':3, 'i':1, 's':1, 'o':1, 'n':1, 'h':1, 'r':1, 'e':3, ' ': 4}
    self.sentence = 'cat is on the tree'

  def test_anagramm_is_true(self):
    self.assertTrue(anagramm('alma', 'mala'))
  def test_anagramm_is_true_if_numbers(self):
    self.assertFalse(anagramm(2516, 1256))
  def test_counter(self):
    self.assertDictContainsSubset(count_letters(self.sentence), self.dictionary)


if __name__ == '__main__':
    unittest.main()
