'use strict';

function range(from, to, step) {
  var output = [];
  if (step > 0) {
    for (var i = from; i < to; i += step) {
      output.push(i);
    }
  } else {
    for (var i = from; i > to; i += step) {
      output.push(i);
    }
  }
  return output;
}



var array = range(4, 8, 2);
console.log(array); // [4, 6]
var array = range(8, 4, -1);
console.log(array); // [4, 6]
