'use strict';
// 1
var car = {
  km: 120000,
  ride: function(km) {
    this.km += km;
  }
};

car.ride(220);
console.log(car.km);

// 2
function createCar(km) {
  return {
    km: km,
    ride: function(km) {
      this.km += km;
    }
  };
}

var skoda = createCar(120000);
var tesla = createCar(2000);
tesla.ride(22);
console.log(tesla.km);

// 3

function ride(km) {
  this.km += km;
};

function Car(km) {
  this.km = km;
  this.ride = ride; 
}

var humvee = new Car(50000);
humvee.ride(12);
console.log(humvee.km);

var bicikli = {
  km: 20,
  isCool: true,
  rideWithFeet: ride
}

bicikli.rideWithFeet(5);
console.log(bicikli);

