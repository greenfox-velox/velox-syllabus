class Car:
    def __init__(self, color, car_type, km):
        if type(color) != str:
            raise Exception('Color is not a string')
        self.color = color
        self.type = car_type
        self.km = km

    def ride(self, km):
        self.km += km

    def getMiles(self):
        return self.km * 0.6213


tesla = Car('pink', 'Tesla S', 1200)

tesla.ride(220)

tesla.has_eye_brows = True

lada = Car('red', 'Lada 1200', 40000)

print(tesla.has_eye_brows)
tesla.ride(300)
print(tesla.getMiles())
