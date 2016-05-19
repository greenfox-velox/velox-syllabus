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
if b == True
  ...
while b == False
  ...
```
