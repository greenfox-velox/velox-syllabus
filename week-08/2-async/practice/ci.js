'use strict';

var students = [
  'Zsolt',
  'Judit',
  'Matyi',
  'Flori'
];


function getRandomFromArray(list) {
  var index = Math.floor(Math.random() * list.length);
  return list[index];
}


console.log(getRandomFromArray(students));
