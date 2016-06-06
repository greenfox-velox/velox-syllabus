from task import Task
from fileio import read_todos_from_file, write_todos_to_file
from printer import print_usage, print_todos

def todo_list_controller():
  todos = read_todos_from_file()
  out = print_todos(todos)
  print(out)

def usage_controller():
  out = print_usage()
  print(out)

def todo_add_controller(new_todo):
  try:
    todos = read_todos_from_file()
    todos.append(Task(text=new_todo))
    write_todos_to_file(todos)
  except TypeError:
    print('Unable to add: No task is provided')

def todo_remove_controller(param):
  try:
    remove_index = int(param) - 1
    todos = read_todos_from_file()
    del todos[remove_index]
    write_todos_to_file(todos)
  except TypeError:
    print('Unable to remove: No index is provided')
  except ValueError:
    print('Unable to remove: Index is not a number')
  except IndexError:
    print('Unable to remove: Index is out of bound')
    
def todo_check_controller(param):
  try:
    check_index = int(param) - 1
    todos = read_todos_from_file()
    todos[check_index].checked = True
    write_todos_to_file(todos)
  except TypeError:
    print('Unable to remove: No index is provided')
  except ValueError:
    print('Unable to remove: Index is not a number')
  except IndexError:
    print('Unable to remove: Index is out of bound')
    
 
  
