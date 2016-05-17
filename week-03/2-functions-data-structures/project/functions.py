def greetFox():
  print("Hello Green Fox!")

greetFox()
greetFox()


# function arguments

def greetByName(name):
  print("Szia,", name)

greetByName("Tojas")
greetByName("Barbi")


# default values for function arguments

def greet(greet="Szia", name="Valaki"):
  print(greet, name)

greet("hello", "Tojas")
greet("szevasz", "Barbi")
greet("csa")
greet(name="Mindenki")


# function return values

def makeGreen(name):
  newName = "Zold " + name
  return newName

name = makeGreen("Tojas")
greetByName(name)
