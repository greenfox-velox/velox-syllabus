class FibonacciIterator:
  def __init__(self, count):
    self.count = count
    self.i = 0
    self.a = 0
    self.b = 1
    self.curr = 0

  def next(self):
    if self.i >= self.count:
      return False

    self.i += 1
    self.curr = self.a
    self.a, self.b = self.a + self.b, self.a
    return True

  def current(self):
    return self.curr

fibo = FibonacciIterator(5)
while fibo.next():
  print(fibo.current())

class Iterator:
  def __init__(self, list):
    self.list = list
    self.i = 0

  def next(self):
    self.i += 1
    return len(self.list) >= self.i

  def current(self):
    return self.list[self.i-1]

print('*' * 80)
l = [1,2,3,4]
iter = Iterator(l)
while iter.next():
  print(iter.current())

