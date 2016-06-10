class Animal(object):
  def __init__(self):
    self.stomach = 0
    self.foodType = ''
    self.race = ''

  def eat(self, food):
    if food != self.foodType:
      raise Exception('Bleeeee')
    self.stomach += 1
    print('I am a ' + self.race + ' thanks for the: ' + self.foodType)

  def poop(self):
    if self.stomach != 0:
      self.stomach -= 1
      print('My poop smells of: ' + self.foodType)
    else:
      print('LOL did not poop...')

class Okapi(Animal):
  def __init__(self):
    super().__init__()
    self.race = 'okapi'
    self.foodType = 'shrooms'

class Platypus(Animal):
  def __init__(self):
    super().__init__()
    self.race = 'platypus'
    self.foodType = 'shrimp'


class Zoo(object):
  def __init__(self, animals):
    self.animals = animals
    self.food = {
      "shrimp": 4,
      "shrooms": 3
    }
  
  def feed(self):
    self.animals[0].stomach = -1
    for animal in self.animals:
      currentFood = ''
      if type(animal) == Okapi:
        currentFood = 'shrooms'
      else:
        currentFood = 'shrimp'
      animal.eat(currentFood)
      self.food[currentFood] -= 1
      if self.food[currentFood] == 0:
        raise Exception('Fuck we run out of: ' + currentFood)
      animal.poop()

budapesti_allat_es_novenykert = Zoo([Platypus()])
budapesti_allat_es_novenykert.feed()
budapesti_allat_es_novenykert.feed()
budapesti_allat_es_novenykert.feed()
print(budapesti_allat_es_novenykert.food)
