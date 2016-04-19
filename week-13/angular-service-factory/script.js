'use strict';

angular.module('todo', [])
  .controller('AddItem', function($scope, todosServ) {
    $scope.addTodo = function (newTodo) {
      todosServ.addTodo(newTodo);
    }
  })
  .controller('ListItems', function kacsa($scope, todosServ) {
    $scope.getTodos = function() {
      return todosServ.getTodos();
    };
  })
  .factory('todosFact', function() {
    var todos = [];
    return {
      getTodos: function() {
        return todos;
      },
      addTodo: function(t) {
        todos.push(t);
      }
    };
  })
  .service('todosServ', function() {
    this.todos = [];
    this.getTodos = function() {
      return this.todos;
    }
    this.addTodo = function(t) {
      this.todos.push(t);
    }
  })
  .value('todos', []);

