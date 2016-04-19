'use strict';

function printEverything(a, b, c) {
  console.log(a, b, c, this);
}

printEverything(1, 2, 3)

var obj = {
  kacsa: 1,
  printEverything: printEverything
}

obj.printEverything(1, 2, 3);

console.log('=========================')

var obj2 = {kitt: 'szaljbeakocsiba'};

printEverything.call(obj2, 1, 2, 3);
printEverything.apply(obj2, [4, 5, 6])

console.log('=========================');

var binded = printEverything.bind(obj2);
binded(7, 8, 9);





var animal = {
  saying: 'Wuff',
  say: function(other) {
    console.log(this.saying + ' ' + other);
  },
  sayMultiple: function(others) {
    others.forEach((function(other) {
      this.say(other);
    }).bind(this)); 
  }
}

animal.sayMultiple(['Tibi', 'Kati']);




var cat = {
  name: 'Cirmi',
  meow: function() {
    console.log('Meow ' + this.name);
  }
};

var dog = {
  name: 'Morzsi',
  bark: function() {
    console.log('Wuff ' + this.name);
  }
};

cat.meow.call(dog);











