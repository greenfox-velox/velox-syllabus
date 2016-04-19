'use strict';


var url = "https://mysterious-dusk-8248.herokuapp.com/todos";
var todoContainer = document.querySelector('.todo-container');

var listCallback = function (response) {
  var todoItems = JSON.parse(response);
  todoItems.forEach(function(todoItem){
    var newTodoItem = document.createElement('p');
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
  })
}

var refresh = function () {
  createRequest('GET', url, {}, listCallback);
}

refresh();

var newTodo = JSON.stringify({text: 'ajajajajjj majom'});
var createTodoCallback = function (response) {
  refresh();
}

createRequest('POST', url, newTodo, createTodoCallback);
