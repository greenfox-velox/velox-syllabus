class TodoItem:
  def __init__(self, id, completed, description):
    self.id = id
    self.completed = completed
    self.description = description

  def format(self, formatter):
    return formatter.format(self)

  def __repr__(self):
    return "<item.TodoItem id={} completed={} description={}>".format(self.id, self.completed, self.description)

class ItemFormatter:
  def format(self, item):
    if item.completed:
      state = "[x]"
    else:
      state = "[ ]"

    return "{} {}".format(state, item.description)

class ChooseItemFormatter:
  def format(self, item):
    return "{}: {}".format(item.id, item.description)
