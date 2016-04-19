from character import Character

class Monster(Character):
    def strike(self, opponent):
        self.hp += 2
        super().strike(opponent)
