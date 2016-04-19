class Warrior:
  def __init__(self):
    self.companions = []
    self.hp = 100

  def join(self, companion):
    self.companions.append(companion)

  def strike(self, oppenent):
    oppenent.inflict_demage(10)

  def curse(self, opponent):
    opponent.join(Curse())
    self._notify_all("curse")

  def inflict_demage(self, demage):
    self.hp -= demage
    self._notify_all("demage")

  def heal(self, hp):
    self.hp += hp

  def _notify_all(self, type):
    for companion in self.companions:
      companion.notify(type, self)

class Healer:
  def notify(self, type, warrior):
    if type == "demage":
      warrior.heal(10)

class Curse:
  def notify(self, type, warrior):
    if type == "demage":
      warrior.heal(-10)

class Cheer:
  def notify(self, type, warrior):
    if type == "curse":
      print("Hurray!!")

rabbit = Warrior()
wolf = Warrior()
shaman = Healer()

rabbit.join(shaman)
wolf.join(Cheer())

wolf.curse(rabbit)
wolf.strike(rabbit)
print(rabbit.hp)
