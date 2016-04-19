'use strict';

function PowerRanger(color) {
  this.color = color;
}

function Fighter() {
  this.isPowerfull = true;
}

PowerRanger.prototype = new Fighter();

var yellowRanger = new PowerRanger('yellow');

console.log(yellowRanger.color);
console.log(yellowRanger.isPowerfull);
