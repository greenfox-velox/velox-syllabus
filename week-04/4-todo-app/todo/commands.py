import sys
import item

class AddItem:
  def invoke(self, store):
    desc = input("Description: ")
    store.add(desc)
    return Result(True)

class CompleteItem:
  def invoke(self, store):
    choice, todoitem = choose_item(store)
    if todoitem:
      todoitem.completed = True
      return Result(True)

    return Result(False, text = "No item for {}".format(choice))

class RemoveItem:
  def invoke(self, store):
    choice, todoitem = choose_item(store)
    if todoitem:
      store.remove(todoitem)
      return Result(True)

    return Result(False, text = "No item for {}".format(choice))

class ListItems:
  def __init__(self, formatter=item.ItemFormatter()):
    self.formatter = formatter

  def invoke(self, store):
    print("Items")
    print("-----")
    for item in store.items:
      print(item.format(self.formatter))
    return Result(True)

class Exit:
  def invoke(self, store):
    store.save()
    sys.exit(0)

class NotImplemented:
  def invoke(self, store):
    return Result(False, text = "This command is not implemented")

def choose_item(store):
  ListItems(item.ChooseItemFormatter()).invoke(store)
  choice = input("Chose one: ")
  try:
    return choice, store.get(int(choice))
  except ValueError:
    print("Error: invalid number")
    return choice, None

class Result:
  def __init__(self, success, text=None):
    self.success = success
    self.text = text
