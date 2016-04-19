'use strict';

function createCar(color, type, km) {
  return {
    color: color,
    type: type,
    km: km,
    ride: function(km) {
      this.km += km;
    }
  };
}

var volvo = createCar('sarga', 'Volvo Markolo', 500);
volvo.ride(50);
console.log(volvo.km);
