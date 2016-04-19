import unittest
from monster import Monster

class TestMonster(unittest.TestCase):
    def test_existance(self):
        monster = Monster('Mike Wazowski', 20, 1)

    def test_inheritance(self):
        monster = Monster('Mike Wazowski', 20, 1)
        self.assertEqual(monster.hp, 20)

    def test_strike(self):
        monster = Monster('Mike Wazowski', 20, 1)
        opponent = Monster('Randall', 10, 2)
        monster.strike(opponent)
        self.assertEqual(monster.hp, 22)
        self.assertEqual(opponent.hp, 9)

unittest.main()
