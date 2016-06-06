import sys
from controllers import *

def main():
  if is_no_command():
    usage_controller()
  elif is_command('a'):
    todo_add_controller(get_param())
  elif is_command('r'): 
    todo_remove_controller(get_param())
  elif is_command('l'):
    todo_list_controller()
  elif is_command('c'):
    todo_check_controller(get_param())

def is_command(command_name):
  return sys.argv[1][1] == command_name

def get_param():
  if len(sys.argv) > 2:
    return sys.argv[2]
  return None

def is_no_command():
  return len(sys.argv) == 1
main()
