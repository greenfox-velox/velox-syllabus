import unittest
from barbarian import Barbarian

class TestBarbarian(unittest.TestCase):
    def test_existance(self):
        barbarian = Barbarian('Conan', 100, 10)

    def test_inheritance(self):
        barbarian = Barbarian('Conan', 100, 10)
        self.assertEqual(barbarian.hp, 100)

    def test_strike(self):
        barbarian = Barbarian('Conan', 100, 10)
        opponent = Barbarian('Herkules', 100, 10)
        barbarian.strike(opponent)
        self.assertEqual(opponent.hp, 80)


unittest.main()
