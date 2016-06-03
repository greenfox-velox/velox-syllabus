import unittest
from cab import CAB

class TestCab(unittest.TestCase):
  def setUp(self):
    self.game = CAB()

  def assert_game(self, random_num, guess, response):
    self.game.number = random_num
    r = self.game.guess(guess)
    self.assertEqual(r, response)

  def test_random(self):
    self.assertEqual(type(self.game.number), list)

  def test_4digit_number(self):
    self.assertEqual(len(self.game.number), 4)

  def test_random_digits(self):
    for digit in self.game.number:
      self.assertTrue(digit >= 0)
      self.assertTrue(digit < 10)
      self.assertEqual(type(digit), int)

  def test_inital_state(self):
    self.assertEqual(self.game.state, 'playing')

  def test_inital_count(self):
    self.assertEqual(self.game.count, 0)

  def test_count_increment(self):
    self.game.guess([0,0,0,0])
    self.assertEqual(self.game.count, 1)

  def test_win(self):
    response = self.game.guess(self.game.number)
    self.assertEqual(response, ['cow', 'cow', 'cow', 'cow'])

  def test_no_match(self):
    self.assert_game([0,0,0,0], [1,1,1,1], [])

  def test_one_match(self):
    self.assert_game([1,0,0,0], [1,2,2,2], ['cow'])

  def test_two_matches(self):
    self.assert_game([1,0,1,0], [1,2,1,2], ['cow', 'cow'])
    


unittest.main()
