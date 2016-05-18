def greet_fox():
  print("Hello Green Fox!")

greet_fox()
greet_fox()


# function arguments

def greet_by_name(name):
  print("Szia,", name)

greet_by_name("Tojas")
greet_by_name("Barbi")


# default values for function arguments

def greet(greet="Szia", name="Valaki"):
  print(greet, name)

greet("hello", "Tojas")
greet("szevasz", "Barbi")
greet("csa")
greet(name="Mindenki")


# function return values

def make_green(name):
  new_name = "Zold " + name
  return new_name

name = make_green("Tojas")
greet_by_name(name)
