# Monday - Expressions and Control flow

## Reqiuired installs
 - Please install Python 3.5
https://www.python.org/downloads/

## Materials for this day
### Must have
 - https://www.youtube.com/watch?v=HBxCHonP6Ro
 - https://www.youtube.com/watch?v=hnxIRVZ0EyU
 - https://www.youtube.com/watch?v=nefopNkZmB4
 - https://www.youtube.com/watch?v=YbipxqSKx-E
 - https://www.youtube.com/watch?v=1yUn-ydsgKk
 - https://www.youtube.com/watch?v=bk22K1m0890
 - https://www.youtube.com/watch?v=llguiJHU0kk
 - https://www.youtube.com/watch?v=Neir-vgPyxw
 - https://www.youtube.com/watch?v=k6rkvgQkW04
 - https://www.youtube.com/watch?v=68EhtQbgXRc


### Nice to have
 - https://www.codecademy.com/courses/introduction-to-python-6WeG3/0/3
 - https://www.codecademy.com/courses/python-beginner-GB6hM/0/1
 - https://www.codecademy.com/courses/python-beginner-sRXwR/0/1
 - https://www.codecademy.com/courses/python-beginner-BxUFN/1/1

## Workshop

### Hello World
```python
print('Hello world')
```

### Numbers
```pyhton
1
0
123
-1
1.1
1.0

1 + 1
2 - 1
3 * 4
1 / 2
1 / 0
1 // 2
1 % 2
2 ** 10
(1 + 3) * 4
```

### Variables
```python
a = 1
a
a = a + 1
a += 1
```

#### Excercises
 - [01.py](workshop/01.py)
 - [02.py](workshop/02.py)
 - [03.py](workshop/03.py)
 - [04.py](workshop/04.py)
 - [05.py](workshop/05.py)
 - [06.py](workshop/06.py)


### Boolean
```python
a == 2
True
False
1 < 2
1 > 2
1 == 2
1 != 2
True or False
True and False
not True

type(1)
type(1 == 1)
```

#### Excercises
 - [07.py](workshop/07.py)
 - [08.py](workshop/08.py)
 - [09.py](workshop/09.py)
 - [10.py](workshop/10.py)
 - [11.py](workshop/11.py)

### Strings
```python
"alma"
""
type("alma")
"alma" + "fa"
"alma" - "fa"
"alma" + 3
"alma" + str(3)
"alma" * 3
"a" in "alma"
len("alma")
"alma"[1]
"alma"[1:3]
int("123")
```

#### Excercises
 - [12.py](workshop/12.py)
 - [13.py](workshop/13.py)
 - [14.py](workshop/14.py)
 - [15.py](workshop/15.py)

### Arrays
```python
[1, 2, 3]
[]
[1, 2] + [3]
[1] - [2]
[1, 2] * 3
1 in [1, 2]
len([1, 2, 3])
arr = [1, 2, 3]
arr[0]
arr[1:3]
[] is []
```

#### Excercises
 - [16.py](workshop/16.py)
 - [17.py](workshop/17.py)
 - [18.py](workshop/18.py)
 - [19.py](workshop/19.py)
 - [20.py](workshop/20.py)

### None
```python
None
```

### If
```python
if a == 2:
    print(a)


if a == 2:
    print("two")
else:
    print("other")


if a == 1:
    print("one")
elif x == 2:
    print("two")
else:
    print("a lot")

if a == 1:
    pass
else:
    print("not one")
```

#### Excercises
 - [21.py](workshop/21.py)
 - [22.py](workshop/22.py)
 - [23.py](workshop/23.py)
 - [24.py](workshop/24.py)
 - [25.py](workshop/25.py)
 - [26.py](workshop/26.py)
 - [27.py](workshop/27.py)
 - [28.py](workshop/28.py)
 - [29.py](workshop/29.py)
 - [30.py](workshop/30.py)


### While
```python
a = 0
while a < 5:
    a += 1
    print(a)
```

#### Excercises
 - [31.py](workshop/31.py)
 - [32.py](workshop/32.py)
 - [33.py](workshop/33.py)
 - [34.py](workshop/34.py)
 - [35.py](workshop/35.py)
 - [36.py](workshop/36.py)
 - [37.py](workshop/37.py)
 
### For
```python
for i in [1, 2, 3, 4]:
    print(i)

for i in range(0, 4):
    print(i)
```

#### Excercises
Please redo the While excercises with for
 - [38.py](workshop/38.py)

### break & continue
```python
numbers = [5, 7, 9, 11, 13, 12]

i = 0
while i < len(numbers):
    if numbers[i] % 3 != 0:
        pass
    else:
        print(numbers[i])
        break
    i += 1



numbers = [5, 7, 9, 11, 13, 12]

i = 0
while i < len(numbers):
    if numbers[i] % 3 != 0:
        continue
    else:
        print(numbers[i])
    i += 1
```
