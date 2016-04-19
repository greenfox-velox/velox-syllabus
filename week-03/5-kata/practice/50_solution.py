# Create a Rectangle class
# It should take a, b as the length of the sides as arguments on the constructor
# It should have a get_perimeter method that returns the perimeter of the Rectangle
# It should have a get_aera method that returns the aera of thi Rectangle

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return self.a * 2 + self.b * 2

    def get_perimeter(self):
        return self.a * self.b
