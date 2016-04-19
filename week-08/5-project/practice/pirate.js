'use strict';

var pirates = [
  {name: 'Jack', id: 1},
  {name: 'Bob', id: 2},
  {name: 'Omar', id: 3},
  {name: 'Olaf', id: 4},
  {name: 'Boris', id: 5}
];

var stashes = [
  {pirateId: 3, gold: 4},
  {pirateId: 4, gold: 1},
  {pirateId: 2, gold: 5},
  {pirateId: 5, gold: 3},
  {pirateId: 1, gold: 8}
];


function getGoldByPirateName(pirateName) {
  var pirateId;
  for (var i = 0; i < pirates.length; i++) {
    if (pirates[i].name === pirateName) {
      pirateId = pirates[i].id;
    }
  }
  for (var j = 0; j < stashes.length; j++) {
    if (stashes[j].pirateId === pirateId) {
      return stashes[j].gold;
    }
  }
}


console.log(getGoldByPirateName('Olaf')); // -> 1

