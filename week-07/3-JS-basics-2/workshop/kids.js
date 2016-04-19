'use strict';
var kids = [
  {name: 'Tibbor', candies: 2},
  {name: 'Steve', candies: 3},
  {name: 'Agoston', candies: 0},
  {name: 'Julika', candies: 7},
  {name: 'Krisztian', candies: 4}
];

function getRichestKidsName(kids) {
  var richestKid = kids[0];
  for (var i = 1; i < kids.length; i++) {
    var currentKid = kids[i];
    if (currentKid.candies > richestKid.candies) {
      richestKid = currentKid;
    }
  }
  return richestKid.name;
}


function getRichestKidsName2(kids) {
  var richestKid = kids[0];
  kids.forEach(function(currentKid) {
    if (currentKid.candies > richestKid.candies) {
      richestKid = currentKid;
    }
  });
  return richestKid.name;
}




console.log(getRichestKidsName2(kids)); // Julika
