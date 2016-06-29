'use strict';

function range(from, to) {
  var output = [];
  for (var i = from; i < to; i++) {
    output.push(i);
  }
  return output;
}

var array = range(3, 7);
console.log(array); // [3, 4, 5, 6]
