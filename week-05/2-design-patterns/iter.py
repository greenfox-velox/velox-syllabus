# Docs:
#   iter: https://docs.python.org/3/library/functions.html#iter
#   iterator: https://docs.python.org/3/glossary.html#term-iterator

class TodoList:
  def __init__(self):
    self.items = []

  def add(self, text):
    self.items.append(text)

  def __iter__(self):
    return TodoListIterator(self)

class TodoListIterator:
  def __init__(self, todo_list):
    self.index = 0
    self.items = todo_list.items

  def __next__(self):
    if self.index < len(self.items):
      item = self.items[self.index]
      self.index += 1
      return item

    raise StopIteration()

todo_list = TodoList()
todo_list.add('Buy milk')
todo_list.add('Cook dinner')
todo_list.add('Save the world')

print(list(todo_list))
for text in todo_list:
  print(text)


class Fibonacci:
  def __init__(self, count):
    self.i = 0
    self.count = count
    self.a = 0
    self.b = 1

  def __iter__(self):
    return self

  def __next__(self):
    if self.i >= self.count:
      raise StopIteration()

    curr = self.a
    self.a, self.b = self.b, self.a + self.b
    self.i += 1
    return curr

print(list(Fibonacci(10)))
for n in Fibonacci(30):
  print(n, end=', ')

print()
