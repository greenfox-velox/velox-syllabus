'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];

function getAges(kids) {
  var ages = [];
  kids.forEach(function(kid) {
    ages.push(kid.age);
  });
  return ages;
}

function getAges2(kids) {
  return kids.map(function(kid) {
    return kid.age;
  });
}

console.log(getAges(kids)); // [8, 7, 6, 9, 8]

