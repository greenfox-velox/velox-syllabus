'use strict';

function substract(a, b) {
  return a - b;
}

function add(a, b) {
  return a + b;
}


function runFunction(fun, a, b) {
  console.log(typeof fun);
  console.log(fun(a, b));
}

runFunction(function(a, b) {
  return a / b;
}, 4, 8);


