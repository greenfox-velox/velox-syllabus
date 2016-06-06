class Vehicle():
  def __init__(self, km):
    self.km = km
  
  def ride(self, km):
    self.km += km

  def print_km(self):
    print('KM:' + str(self.km))

roller = Vehicle(24)
roller.ride(11)
roller.print_km()

class Car(Vehicle):
  def __init__(self, km, gas):
    super().__init__(km)
    self.gas = gas

  def ride(self, km):
    super().ride(km)
    self.gas -= km
  
  def print_gas(self):
    print('GAS:' + str(self.gas))

  def print_stats(self):
    self.print_km()
    self.print_gas()

trabant = Car(120000, 50)
trabant.ride(11)
trabant.print_stats()
