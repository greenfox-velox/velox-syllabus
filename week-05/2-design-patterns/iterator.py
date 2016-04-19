class DoubleIterator:
  def __init__(self, n=1):
    self.n = n

  def next(self):
    self.n *= 2
    return True

  def current(self):
    return self.n

class FibonacciIterator:
  def __init__(self, count):
    self.a = 0
    self.b = 1
    self.i = 0
    self.count = count
    self.curr = 0

  def next(self):
    if self.i >= self.count:
      return False

    self.curr = self.a
    self.a, self.b = self.b, self.a + self.b
    self.i += 1
    return True

  def current(self):
    return self.curr

class DoubleListIterator:
  def __init__(self, list):
    self.index = -1
    self.list = list

  def next(self):
    self.index += 1
    return self.index < len(self.list)

  def current(self):
    return self.list[self.index] * 2

class Item:
  def __init__(self, text):
    self.text = text

class ItemList:
  def __init__(self):
    self.items = []

  def add(self, text):
    item = Item(text)
    self.items.append(item)

  def iterator(self):
    return ItemTextIterator(self)

class ItemTextIterator:
  def __init__(self, item_list):
    self.index = -1
    self.item_list = item_list

  def next(self):
    self.index += 1
    return self.index < len(self.item_list.items)

  def current(self):
    item = self.item_list.items[self.index]
    return item.text


iter = DoubleIterator()
print((iter.next(), iter.current()))
print((iter.next(), iter.current()))
print((iter.next(), iter.current()))
print((iter.next(), iter.current()))

print('=' * 80)

fibo = FibonacciIterator(10)
while fibo.next():
  print(fibo.current(), end=', ')

print()
print('=' * 80)

iter = DoubleListIterator([1,2,3,4])
while iter.next():
  print(iter.current())

print('=' * 80)

item_list = ItemList()
item_list.add('Apple')
item_list.add('Orange')
item_list.add('Peach')

iter = item_list.iterator()
while iter.next():
  print(iter.current())

