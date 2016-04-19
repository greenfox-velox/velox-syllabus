from character import Character

class Barbarian(Character):
    def strike(self, opponent):
        opponent.hp -= self.damage * 2
