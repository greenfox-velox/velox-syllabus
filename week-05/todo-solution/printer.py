def print_usage():
    usage = '''
Python Todo application
=======================

Command line arguments:
 -l   Lists all the tasks
 -a   Adds a new task
 -r   Removes an task
 -c   Completes an task
    '''
    return usage

def print_todos(todos):
  if len(todos) == 0:
    return 'No todos for today!'
  todolist = ''
  i = 0
  for todo in todos:
    i += 1
    todolist += str(i) + ' - ' + todo.to_string() + '\n'
  return todolist

