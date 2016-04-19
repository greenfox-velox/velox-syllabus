'use strict';

var g = 123;

function printG() {
  console.log(g);
  g = 333;
}

printG();
console.log(g);




function printLocalG() {
  var g = 7;
  console.log(g);
}

printLocalG();
console.log(g);












function printA() {
  var a = 123;
  console.log(a);
}

printA();
// console.log(a); ERROR


if (true) {
  var c = 999;
}
console.log(c);


for (var i = 0; i < 3; i++) {
  console.log('csa');
}

for (; i < 5; i++) {
  console.log('asasa');
}
