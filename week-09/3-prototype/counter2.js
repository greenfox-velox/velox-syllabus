'use strict';

function createCounter(start) {
  return function() {
    start++;
    return start;
  }
}

var counter = createCounter(5);
console.log(counter());
console.log(counter());

var counter2 = createCounter(0);
console.log(counter2());
