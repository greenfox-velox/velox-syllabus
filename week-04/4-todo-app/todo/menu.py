import io
import commands

def classic_menu():
  items = [
    MenuItem("1", "List items", commands.ListItems()),
    MenuItem("2", "Add new item", commands.AddItem()),
    MenuItem("3", "Complete an item", commands.CompleteItem()),
    MenuItem("4", "Remove an item", commands.RemoveItem()),
    MenuItem("0", "Save and exit", commands.Exit()),
  ]
  return Menu(items)

class Menu:
  def __init__(self, choices, formatter=None):
    self.formatter = formatter or DefaultMenuItemFormatter()
    self.choices = choices

  def display(self):
    with io.StringIO() as buf:
      for item in self.choices:
        buf.write(item.display(self.formatter) + "\n")
      return buf.getvalue()

  def invoke(self, choice, store):
    for item in self.choices:
      if item.option == choice:
        return item.invoke(store)

    return commands.Result(success=False, text="No such option: {}".format(choice))

class DefaultMenuItemFormatter:
  def format(self, item):
    return "{}: {}".format(item.option, item.text)

class MenuItem:
  def __init__(self, option, text, cmd):
    self.option = option
    self.text = text
    self.command = cmd

  def display(self, formatter):
    return formatter.format(self)

  def invoke(self, store):
    return self.command.invoke(store)
