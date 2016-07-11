'use strict';

function honk() {
  console.log(this);
  var _this = this;
  [1, 2, 3, 4].forEach(function() {
    console.log(_this);
  });
}

var car = {
  km: 40000,
  honk: honk
};

car.honk();
honk();


