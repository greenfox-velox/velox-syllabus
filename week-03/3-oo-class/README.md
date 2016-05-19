# Wednesday - Object Oriented Programming

## Before lesson materials

Mandatory:

 - https://www.youtube.com/watch?v=POQIIKb1BZA
 - https://www.youtube.com/watch?v=G8kS24CtfoI
 - https://www.youtube.com/watch?v=qSDiHI1kP98
 - https://www.youtube.com/watch?v=oROcVrgz91Y 

Advised:

 - [Hands-on Python Tutorial: Object Orientation (only section 2.1.1)](http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/strings3.html#object-orientation)
 - [Codecademy course - Introduction to Classes](https://www.codecademy.com/courses/python-intermediate-en-WL8e4/0/1)


## Workshop
### Class and Constructor

```python
rectangle1 = {"a": 40, "b": 50}
rectangle2 = {"a": 20, "b": 30}

def get_circumference(rect):
  return rect["a"] * 2 + rect["b"] * 2

print(get_circumference(rectangle1))
print(get_circumference(rectangle2))
```

```python
class Rectangle():
  a = 0
  b = 0
  
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def get_circumference(self):()
    return self.a * 2 + self.b * 2

rect1 = Rectangle(40, 50)
rect2 = Rectangle(20, 30)
print(rect1.get_circumference())
print(rect2.get_circumference())

```
[01.py](01.py)
[02.py](02.py)
[03.py](03.py)
[04.py](04.py)
[05.py](05.py)

#### List functions

```python
my_list = [1, 2, 3]
my_list.append(4)
my_list.pop()
```

[06.py](06.py)
[07.py](07.py)

### Inheritance
```python
class Base():
  a = 0

  def printA(self):
    print("a is:" + str(self.a))

class Child(Base):
  b = 1

  def printB(self):
    print("b is:" + str(self.b))

  def printAll(self):
    self.printA()
    self.printB()

child = Child()
child.a = 12
child.b = 24
```
[08.py](08.py)

#### Practice
[09.py](09.py)
[10.py](10.py)
[11.py](11.py)

