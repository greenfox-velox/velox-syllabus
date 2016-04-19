'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];


function filterNamesBySex(kids, gender) {
  var filteredNames = [];
  kids.forEach(function(kid) {
    if (kid.sex === gender) {
      filteredNames.push(kid.name);
    }
  });
  return filteredNames;
}


console.log(filterNamesBySex(kids, 'female')); // ['Julika', 'Gerda']

