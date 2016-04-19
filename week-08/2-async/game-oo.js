'use strict';

function Game() {
  var _this = this;
  this.candies = 0;
  this.lollypops = 0;
  this.price = 10;

  this.updateCandies = function() {
    document.querySelector('.candies').innerHTML = this.candies;
  };

  this.updateLollypops = function() {
    document.querySelector('.lollypops').innerHTML = this.lollypops;
  };

  this.updateSpeed = function() {
    document.querySelector('.speed').innerHTML = this.getSpeed();
  };

  this.getSpeed = function() {
    return Math.floor(this.lollypops / this.price);
  };

  this.init = function() {
    document.querySelector('.create-candies').addEventListener('click', function() {
      _this.candies++;
      _this.updateCandies()
    });

    document.querySelector('.buy-lollypops').addEventListener('click', function() {
      if (_this.candies > _this.price) {
        _this.lollypops++;
        _this.candies -= _this.price;
        _this.updateLollypops();
        _this.updateCandies()
        _this.updateSpeed(_this.getSpeed());
      }
    });

    setInterval(function () {
      _this.candies += _this.getSpeed();
      _this.updateCandies();
      if (_this.candies === 10000) {
        alert('WIN!');
      }
    }, 1000);
  };
}

var game = new Game();
game.init();

