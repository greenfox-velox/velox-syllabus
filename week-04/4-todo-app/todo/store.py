import json
import os
from item import TodoItem

class Store(object):
  def __init__(self, path, backend='json'):
    self.id_gen = IdGenerator()
    self.backend = backends[backend](self)
    self.path = path
    self.items = []

  def add(self, description):
    item = TodoItem(self.id_gen.next(), False, description)
    self.items.append(item)
    return item

  def remove(self, item):
    self.items.remove(item)

  def get(self, id):
    for item in self.items:
      if item.id == id:
        return item

    return None

  def save(self):
    self.backend.save()

  def load(self):
    if os.path.exists(self.path):
      self.backend.load()
    return self

class IdGenerator:
  def __init__(self, seed=0):
    self.seed = seed

  def next(self):
    self.seed += 1
    return self.seed

class TextBackend:
  def __init__(self, store):
    self.store = store

  def load(self):
    with open(self.store.path) as f:
      for line in f:
        self.store.add(line.rstrip())

  def save(self):
    with open(self.store.path, 'w') as f:
      for item in self.store.items:
        if not item.completed:
          f.write(item.description + '\n')

class JsonBackend:
  def __init__(self, store):
    self.store = store

  def load(self):
    with open(self.store.path) as f:
      items = json.load(f)

    for item in items:
      todoitem = self.store.add(item['description'])
      todoitem.completed = item['completed']

  def save(self):
    items = []
    for item in self.store.items:
      items.append({ 'description': item.description, 'completed': item.completed })
    with open(self.store.path, 'w') as f:
      json.dump(items, f)

backends = {
  'text': TextBackend,
  'json': JsonBackend
}
