# hidden side-effect
g = []
def add(a, b):
  res = a + b
  g.append(res)
  return res

# not so hidden side-effect
n = 1
def add2(a, b):
  global n
  n = a + b
