# Tuesday - Functions and data structures

## Materials for this day

### Must have
 - https://www.youtube.com/watch?v=j2xhtI0WTew
 - https://www.youtube.com/watch?v=xRIzPZlei9I
 - https://www.youtube.com/watch?v=mwr1AtpLMpI
 - https://www.youtube.com/watch?v=f3TVuuhe-fY
 - https://www.youtube.com/watch?v=DASOXeFFkCg
 - https://www.youtube.com/watch?v=QSTo9F8E6GE
 - https://www.youtube.com/watch?v=DJ2HSCT6Z8w
 - https://www.youtube.com/watch?v=j2xhtI0WTew
 - https://www.youtube.com/watch?v=BSNFRKG1MfE

### Nice to have
 - [General introduction to functions][1]
 - [Introduction to Python built-in data structures][2]
 - [Codecademy course on Python functions][4]
 - [Codecademy course on Python lists and dictionaries][5]
 - [Hands-on Python Tutorial: Defining Functions of your Own][3]


## Workshop

### Functions
```python
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

```

#### Excercises
 - [31.py](workshop/31.py)
 - [32.py](workshop/32.py)
 - [33.py](workshop/33.py)
 - [34.py](workshop/34.py)
 - [35.py](workshop/35.py)
 - [36.py](workshop/36.py)
 - [37.py](workshop/37.py)
 - [38.py](workshop/38.py)
 - [39.py](workshop/39.py)


### Function scope
```python
# global scope
n = 2

def f():
  # local scope
  n = 1
  print("local", n)

f() # => 1
print("global", n)

def c():
  r = 1
  print(r)
c()
print(r)

```

### Data structures
```python
giraffe = {'color': 'yellow', 'pattern': 'polygonal patches'}
whale = {'color': 'blue', 'size': 10000}

print(giraffe)
print(giraffe['pattern'])
print(whale['size'])

whale['say'] = 'eeeeeeeeeeeeuuuuuuw'

print(whale)
```


#### Excercises
 - [40.py](workshop/40.py)
 - [41.py](workshop/41.py)

#### PRO
 - [PRO leage](PRO.md)

[1]: http://www.cs.utah.edu/~germain/PPS/Topics/functions.html
[2]: http://pymbook.readthedocs.org/en/latest/datastructure.html
[3]: http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html
[4]: https://www.codecademy.com/en/courses/python-beginner-c7VZg/0/1?curriculum_id=4f89dab3d788890003000096
[5]: https://www.codecademy.com/en/courses/python-beginner-en-pwmb1/0/1?curriculum_id=4f89dab3d788890003000096
