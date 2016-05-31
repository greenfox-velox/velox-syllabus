# Exceptions

## Materials
### Mandatory
 - https://www.youtube.com/watch?v=1cCU0owdiR4 
 - http://pymbook.readthedocs.io/en/latest/exceptions.html

### Optional
 - https://www.youtube.com/watch?v=k50zqdXdYxc


## Workshop
 - [1.py](workshop/1.py)
 - [2.py](workshop/2.py)
 - [3.py](workshop/3.py)

## Project

Write a command-line todo application to easily keep track of your day-to-day tasks.

Basics (mandatory):

Prints usage
A todo item has (at least) a completed state and a description
Add new items
Complete items
Remove items
List items

### Stories

#### Usage
 - Given the terminal opened in the project directory
 - When the application is runned by executing `python todo.py`
 - Then it should print the usage information:
```
Python Todo application
=======================

Command line arguments:
 -l   Lists all the items
 -a   Adds a new item
 -r   Removes an item
 -c   Completes an item
```

##### Help
 - http://www.tutorialspoint.com/python/python_command_line_arguments.htm


#### List
 - Given the terminal opened in the project directory, and a file that stores the todos
 - When the application is runned by executing `python todo.py -l`
 - Then it should print the todos that are stored in the file
```
Walk the dog
Buy milk
Do homework
```
