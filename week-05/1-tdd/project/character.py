class Character():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def drink_potion(self):
        self.hp += 10

    def strike(self, opponent):
        opponent.hp -= self.damage

    def get_status(self):
        life_status = 'DEAD'
        if self.hp > 0:
            life_status = 'HP: ' + str(self.hp)
        return self.name + '\n' + life_status
