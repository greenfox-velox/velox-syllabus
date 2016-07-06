'use strict';

var tape = require('tape');
var carPark = require('./04');

var Car = carPark.Car;
var CarPark = carPark.CarPark;

tape('Car properties', function (t) {
  var car = new Car('volvo', 'red', 50);
  t.equal(car.type, 'volvo');
  t.equal(car.color, 'red');
  t.equal(car.balance, 50);
  t.end();
});

tape('Car id', function (t) {
  var car = new Car('volvo', 'red', 50);
  t.equal(typeof car.id, 'number');
  t.end();
});

tape('Car distinct ids', function (t) {
  var car = new Car('volvo', 'red', 50);
  var car2 = new Car('ifa', 'blue', 10);
  t.notEqual(car.id, car2.id)
  t.end();
});

tape('enter method', function (t) {
  var car = new Car('volvo', 'red', 50);
  car.enter(0);
  t.equal(car.enterDate, 0);
  t.end();
});

tape('getEnterDate method', function(t) {
  var car = new Car('volvo', 'red', 50);
  car.enter(1000);
  t.equal(car.getEnterDate(), 1000);
  t.end();
});

tape('leave method', function(t) {
  var car = new Car('volvo', 'red', 50);
  car.leave(20);
  t.equal(car.balance, 30);
  t.end();
});

tape('getStats method', function(t) {
  var car = new Car('volvo', 'red', 50);
  t.equal(car.getStats(), 'Type: volvo, Color: red, Balance: 50');
  t.end();
});

tape('CarPark properties', function(t) {
  var carPark = new CarPark(1000, 0);
  t.equal(carPark.income, 1000);
  t.equal(carPark.time, 0);
  t.end();
});

tape('carEnter method', function(t) {
  var world = createCarPark(1);
  t.equal(world.carPark.cars.length, 1);
  t.end();
});

tape('carLeave method one car', function(t) {
  var world = createCarPark(1);
  world.carPark.carLeave(world.car.id);
  t.equal(world.carPark.cars.length, 0);
  t.end();
});

tape('carLeave method two cars', function(t) {
  var world = createCarPark(2);
  world.carPark.carLeave(world.car.id);
  t.equal(world.carPark.cars.length, 1);
  t.end();
});

tape('carLeave method delete id', function(t) {
  var world = createCarPark(2);
  world.carPark.carLeave(world.car.id);
  t.equal(world.carPark.cars[0].id, world.car2.id);
  t.end();
});

tape('elapseTime method', function(t) {
  var carPark = new CarPark(1000, 2000);
  carPark.elapseTime(3000);
  t.equal(carPark.time, 5000);
  t.end();
});

tape('carLeave method one car and pay one hour', function(t) {
  var world = createCarPark(1);
  world.carPark.elapseTime(60 * 60 * 1000);
  world.carPark.carLeave(world.car.id);
  t.equal(world.car.balance, 460);
  t.end();
});

tape('carLeave method one car and pay ten hours', function(t) {
  var world = createCarPark(1);
  world.carPark.elapseTime(10 * 60 * 60 * 1000);
  world.carPark.carLeave(world.car.id);
  t.equal(world.car.balance, 100);
  t.end();
});


function createCarPark(carCount) {
  var world = {};
  world.carPark = new CarPark(1000, 0);
  world.car = new Car('volvo', 'red', 500);
  world.carPark.carEnter(world.car);
  if (carCount > 1) {
    world.car2 = new Car('ifa', 'blue', 10);
    world.carPark.carEnter(world.car2);
  }
  return world;
}


