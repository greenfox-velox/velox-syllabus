'use strict';

function createCounter() {
  var count = 0;

  return function() {
    count++;
    return count;
  }
}

var counter = createCounter();
console.log(counter());
console.log(counter());
console.log(counter());
console.log(counter());

var counter2 = createCounter();
console.log(counter2());
console.log(counter2());
