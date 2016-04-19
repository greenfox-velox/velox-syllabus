'use strict';

function sum(numbers) {
  var output = 0;
  for (var i = 0; i < numbers.length; i++) {
    output += numbers[i];
  }
  return output;
}

console.log(sum([4, 5, 6]));
