from character import Character

class Cleric(Character):
    def heal(self, other):
        other.hp += 10
