'use strict';

function greet(name) {
  console.log('Csa-aa ' + name + '!');
}

greet('Tojas');

var koszontes = greet;

koszontes('Gyuri');

var print = console.log;

function greeter(name, log) {
  log('Csovi ' + name);
}

greeter('Lajoskam', print);







var add = function (a, b) { return a + b; };

console.log(add(1, 2));


function customLogger(text) {
  console.log(text, 'logged by my function');
}


greeter('Csabi', customLogger);
