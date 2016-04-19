class Node:
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

root = Node(
  1,
  Node(2), # left
  Node(3)  # right
)

class LeftIterator:
  def __init__(self, root):
    self.curr = root

  def next(self):
    return self.curr is not None

  def current(self):
    temp = self.curr
    self.curr = self.curr.left
    return temp

iter = LeftIterator(root)
while iter.next():
  print(iter.current().value)
