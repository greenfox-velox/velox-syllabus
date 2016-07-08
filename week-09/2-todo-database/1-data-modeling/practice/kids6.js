'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];


function countBySex(kids) {
  var output = {female: 0, male: 0};
  kids.forEach(function(kid) {
    output[kid.sex]++;
  });
  return output;
}

function countBySex2(kids) {
  var output = {};
  kids.forEach(function(kid) {
    if (!(kid.sex in output)) {
      output[kid.sex] = 0;
    }
    output[kid.sex]++;
  });
  return output;
}


console.log(countBySex2(kids)); // {female: 2, male: 3}

