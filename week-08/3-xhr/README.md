# Wednesday - XMLHttpRequest

https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started

# TODO API docs

https://mysterious-dusk-8248.herokuapp.com/

## List todos
- method: GET
- url: /todos
- returns: list of todos

## Create todo
- method: POST
- url: /todos
- request body:
  {
    "text": "Description of the item"
  }
- returns: created todo

## Update todo (set completed)
- method: PUT
- url: /todos/1
- request body:
  {
    "completed": "true"
  }
- returns: updated todo

## Delete todo
- method: DELETE
- url: /todos/1
- returns: deleted todo
