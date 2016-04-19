'use strict';

function greet(name) {
  console.log('Hi ' + name + '!');
}

greet('Tojas');

greet('Tojas', 4, [], {kacsa: 'pulcsiban'})

greet();

function printArgs(a, b, c, d, e) {
  console.log(a, b, c, d, e);
}

printArgs(1, 2, 3);


function double(num) {
  return 2 * num;
}

console.log(double(4));
