class Elem(object):
  __slots__ = ['value', 'next']
  def __repr__(self):
    return '({}, {})'.format(str(self.value), self.next)

def new_elem(value):
  elem = Elem()
  elem.value = value
  elem.next = None
  return elem

def append(head, value):
  elem = last(head)
  new = new_elem(value)
  elem.next = new

  return head

def last(head):
  elem = head
  while elem.next is not None:
    elem = elem.next

  return elem

def at(head, index):
  elem = head
  for i in range(index):
    if elem.next is not None:
      elem = elem.next
    else:
      return None

  return elem

def insert(head, index, value):
  new = new_elem(value)
  if index == 0:
    new.next = head
    return new

  elem = at(head, index-1)
  if elem is None:
    # Something went terribly and horrible wrong
    return head

  old_next = elem.next
  elem.next = new
  new.next = old_next

  return head

def find(head, value):
  elem = head
  while elem is not None and elem.value != value:
    elem = elem.next
  return elem

def remove(head, value):
  prev, elem = None, head

  while elem is not None and elem.value != value:
    prev = elem
    elem = elem.next

  # elem is head
  if prev is None:
    return elem.next

  prev.next = elem.next
  return head

def remove_at(head, index):
  if index == 0:
    return head.next

  prev = at(head, index-1)
  elem = prev.next
  prev.next = elem.next

  return head

def size(head):
  size = 0
  elem = head
  while elem is not None:
    size += 1
    elem = elem.next

  return size

head = new_elem(1)
append(head, 2)
append(head, 3)
append(head, 4)
