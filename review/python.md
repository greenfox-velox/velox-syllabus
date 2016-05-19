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
