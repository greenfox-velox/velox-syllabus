'use strict';

var nameInput = document.getElementById('name');
var caloriesInput = document.getElementById('calories');
var dateInput = document.getElementById('date');
var addButton = document.getElementById('add');
var mealContainer = document.getElementById('meals');
var filterButton = document.getElementById('filter');
var allButton = document.getElementById('all');
var filterDate = document.getElementById('filter-date');
var sumCalories = document.getElementById('sum');

var filter = '';

addButton.addEventListener('click', function (event) {
  var meal = {
    name: nameInput.value,
    calories: caloriesInput.value,
    date: dateInput.value
  };
  sendRequest({
    data: meal,
    method: 'POST',
    url: 'http://localhost:3000/meals'
  }, function(r) {
    console.log(r);
    updateList();
  });
});

mealContainer.addEventListener('click', function (event) {
  if (event.target.classList.contains('delete')) {
    sendRequest({
      url: 'http://localhost:3000/meals/' +event.target.id,
      method: 'DELETE'
    }, function(r) {
      console.log(r);
      updateList();
    });
  }
});

filterButton.addEventListener('click', function (event) {
  filter = filterDate.value;
  updateList();
});

allButton.addEventListener('click', function (event) {
  filter = '';
  updateList();
});

updateList();

function updateList() {
  sendRequest({
    method: 'GET',
    url: 'http://localhost:3000/meals'
  }, function(meals) {
    var sum = 0;
    mealContainer.innerHTML = '';
    meals.filter(function(meal) {
      if (!filter) {
        return true;
      }
      return meal.date.split('T')[0] === filter;
    }).forEach(function(meal) {
      var li = document.createElement('li');
      li.innerHTML = templateMeal(meal);
      mealContainer.appendChild(li);
      sum += meal.calories;
    });
    console.log(sum);
    sumCalories.innerText = sum;
  });
}

function templateMeal(meal) {
  return '<span class="name">' + 
    meal.name +
    '</span><span class="calories">' +
    meal.calories +
    '</span><span class="date">' +
    meal.date +
    '</span>' +
    '<button id="'+ meal.id +'" class="delete">delete</button>';
}


function sendRequest(options, callback) {
  var xhr = new XMLHttpRequest();
  xhr.onload = function(e) {
    callback(JSON.parse(xhr.response));
  };
  xhr.open(options.method, options.url);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(options.data && JSON.stringify(options.data));
}
