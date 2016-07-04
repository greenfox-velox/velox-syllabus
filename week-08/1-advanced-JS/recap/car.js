'use strict';

function Car(km) {
  this.km = km;
}

Car.prototype.ride = function(km) {
  this.km += km;
}

var opel = new Car(40000);

opel.ride(120);

console.log(opel.km);

