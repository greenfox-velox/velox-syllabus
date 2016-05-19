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
[1.py](1.py)
[2.py](2.py)
[3.py](3.py)
[4.py](4.py)
[5.py](5.py)

#### List functions

```python
my_list = [1, 2, 3]
my_list.append(4)
my_list.pop()
```

[6.py](6.py)
[7.py](7.py)

### Inheritance
```python
class Base():
  def __init__(self, a):
    self.a = a
 
  def printA(self):
    print("a is:" + str(self.a))

class Child(Base):
  def __init__(self, a, b);
    self.a = a
    self.b = b

  def printB(self):
    print("b is:" + str(self.b))

  def printAll(self):
    self.printA()
    self.printB()

child = Child(1, 2)
child.printAll()

```
[8.py](8.py)

#### Practice

