# Week 8 - Backend

## Days
- JS OO + TAPE
- Dojo
- Callbacks
- REST

## Project
![Todo mockup](todo-mockup.png)

### Check out the API docs
- https://todo-docs.herokuapp.com/docs/#!/default
- See all the paths
- Examine the parameters and responses
- Try all endpoints

### Try to access the API
- https://mysterious-dusk-8248.herokuapp.com/todos

### Create the form
- HTML
- CSS

### Create the JS
- on page load, get all todos from the API
- when adding a new todo
    - send the todo to the API
    - and also display it in the list for the client (when the response is success)
- when deleting a todo
    - send the delete request to the API
    - and also update the list for the client (when the response is success)
- when completing a todo
    - same in english (just as above)

### Tips & Tricks
- all API calls should be separated
- you can disable a button for the time being
- the API's host should be easily modified
- avoid code duplication
- you should be able to write tests, so do that! :)
