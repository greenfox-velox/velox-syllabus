'use strict';

var array = ['apple', 'pear', 'melon', 'carrot', 'grape'];

function delete1(array) {
  var newArray = [];
  for (var i = 0; i < array.length; i++) {
    if (array[i] !== 'carrot') {
      newArray.push(array[i]);
    }
  }
  array = newArray;
  return array;
}

function delete2(array) {
  var newArray = [];
  array.forEach(function(elem) {
    if (elem !== 'carrot') {
      newArray.push(elem);
    }
  });
  array = newArray;
  return array;
}

function delete3(array) {
  array.splice(array.indexOf('carrot'), 1);
  return array;
}

// Delete carrot from the array 
