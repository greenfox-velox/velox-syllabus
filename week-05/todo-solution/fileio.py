from task import Task

STORAGE_FILE_NAME = 'todo.txt'

def read_todos_from_file():
  lines = strip_newlines(read_lines_from_file())
  todos = []
  for line in lines: 
    task = Task()
    task.set_from_db_line(line)
    todos.append(task)
  return todos

 
def strip_newlines(lines):
  todos = []
  for line in lines:
    todos.append(line.rstrip())
  return todos

def read_lines_from_file():
  file = open(STORAGE_FILE_NAME, 'r')
  lines = file.readlines()
  file.close()
  return lines

def write_todos_to_file(todos):
  file = open(STORAGE_FILE_NAME, 'w')
  for todo in todos:
    file.write(todo.get_to_db_line() + '\n')
  file.close()
