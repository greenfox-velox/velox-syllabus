import random

class Weapon:
  def strike(self, warrior, opponent):
    opponent.hp -= self.demage()
    warrior.hp -= self.self_demage()

  def demage(self):
    raise "Not implmented"

  def self_demage(self):
    raise "Not implmented"

class Sword(Weapon):
  def demage(self):
    return 10

  def self_demage(self):
    return 0

class Flamethrower(Weapon):
  def demage(self):
    return 50

  def self_demage(self):
    return 20

class CriticalSword(Weapon):
  def demage(self):
    return 10 + random.randint(0, 10)

  def self_demage(self):
    return 0

class Enchanted(Weapon):
  def __init__(self, weapon):
    self.weapon = weapon

  def demage(self):
    return self.weapon.demage() * 2

  def self_demage(self):
    return self.weapon.self_demage() / 2

class Warrior:
  def __init__(self, weapon):
    self.weapon = weapon
    self.hp = 100

  def strike(self, opponent):
    self.weapon.strike(self, opponent)

  def __repr__(self):
    return "Warrior hp={}".format(self.hp)

warrior = Warrior(Sword())
monster = Warrior(Flamethrower())

warrior.strike(monster)
print(warrior)
print(monster)

monster.strike(warrior)
print(warrior)
print(monster)

warrior = Warrior(Enchanted(Sword()))
warrior.strike(monster)
print('---')
print(monster)




