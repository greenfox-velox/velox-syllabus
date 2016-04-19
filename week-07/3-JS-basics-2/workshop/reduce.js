'use strict';

var numbers = [5, 6, 3, 9];

function reduceSum(acc, num) {
  return acc + num;
}

var sum = numbers.reduce(reduceSum, 0);

console.log(sum);
