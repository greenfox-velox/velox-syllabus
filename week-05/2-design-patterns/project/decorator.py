class Sword:
  def demage(self):
    return 10

class Enhanced:
  def __init__(self, weapon):
    self.weapon = weapon

  def demage(self):
    return self.weapon.demage() + 5

class Magical:
  def __init__(self, weapon):
    self.weapon = weapon

  def demage(self):
    return self.weapon.demage() * 2

class Rusty:
  def __init__(self, weapon):
    self.weapon = weapon

  def demage(self):
    return self.weapon.demage() / 2

class Warrior:
  def __init__(self, weapon = Sword()):
    self.hp = 100
    self.weapon = weapon

  def strike(self, opponent):
    demage = self.weapon.demage()
    opponent.hp -= demage

warrior = Warrior(Magical(Enhanced(Sword())))
opponent = Warrior()

print(opponent.hp)
warrior.strike(opponent)
print(opponent.hp)

