import unittest
import lottery

class TestPIP(unittest.TestCase):

    def setUp(self):
        self.five_most_frequent = ('+--------+-----------+'
                                   '| number | frequency |'
                                   '+--------+-----------+'
                                   '|   3    |    199    |'
                                   '|   1    |    183    |'
                                   '|   4    |    174    |'
                                   '|   2    |    158    |'
                                   '|   5    |    146    |'
                                   '+--------+-----------+')

    def test_lottery_five_most_frequent(self):
        self.assertEqual(lottery.five_most_frequent(), self.five_most_frequent)

if __name__ == '__main__':
    unittest.main()
