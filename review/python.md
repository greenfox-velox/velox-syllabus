# Python review concerns

## General problems

### Comparing Booleans

If you want to use a boolean variable in an `if` statement, you should just use the variable value itself

```python
b = True
# Good
if b:
  ...
while not b:
  ...

# Bad
if b == True:
  ...
while b == False:
  ...
```

### Iterating through lists

When you need to iterate through a list and do something with all the elements, you should use `foreach` syntax, not with `while` or `for` with indices.
```python
# Good
for element in list:
  print(element)

# Bad
i = 0
size = len(elements)
while i < size:
  print(elements[i])
  i += 1
```

### Indentation in Python

By default the styleguide says indentation should be 4 spaces. Our religion is 2 spaces for all languages, so both of them are acceptable, but __be consistant__!

```python
# Good
def something():
  statement
  if another:
    other_statement

# Good
if something:
    statement
    while another:
        other_statement

# Bad
def another():
        very_deep_statement

# Bad
for i in list:
  if something:
      not_consistant
```

### Drunk born Pirates
There shouldn't be a param for setting the pirates' `rum_num` in the constructor.
Pirates are not created or born to have drunk already something. Every new born pirate is an alcohol virgin. They need to `drink_rum()` to actually increase the number of rums they did consume.
```python
# Good
class Pirate(object):
  def __init__(self):
    self.consumed_rum = 0 # every new born pirate has consumed this amount, there's no way to create a pirate that has already drunk some

# Bad
class Pirate(object):
  def __init__(self, drunken_rum):
    self.consumed_rum = drunken_rum # no way, you shouldn't drink while pregnant
```
_The takeaway from the story is you need to decide what attributes can be set when creating a new object and what have default values_

### Using spaces around operators
Either use on both sides either none of the sides. In the styleguide there are more rules about where to use spaces around operators
```python
# Good
variable = 5 / 6

# Bad
variable= 5 /6
```
