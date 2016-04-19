import unittest
from character import Character

class TestCaracter(unittest.TestCase):
    def test_existance(self):
        character = Character('Test', 100, 10)

    def test_properties(self):
        character = Character('Test', 100, 10)
        self.assertEqual(character.name, 'Test')
        self.assertEqual(character.hp, 100)
        self.assertEqual(character.damage, 10)

    def test_drink_potion(self):
        character = Character('Test', 100, 10)
        character.drink_potion()
        self.assertEqual(character.hp, 110)

    def test_strike(self):
        character = Character('Test', 100, 10)
        opponent = Character('Opponent', 100, 10)
        character.strike(opponent)
        self.assertEqual(opponent.hp, 90)

    def test_get_status_contains_name(self):
        first_line = self.get_status_line(0, 100)
        self.assertEqual(first_line, 'Test')

    def test_get_status_contains_dead(self):
        last_line = self.get_status_line(1, 0)
        self.assertEqual(last_line, 'DEAD')

    def test_get_status_live(self):
        last_line = self.get_status_line(1, 100)
        self.assertEqual(last_line, 'HP: 100')

    def get_status_line(self, line_number, hp):
        character = Character('Test', hp, 10)
        status = character.get_status()
        return status.split('\n')[line_number]
        



unittest.main()
