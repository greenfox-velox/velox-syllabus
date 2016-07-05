'use strict';

var candies = 0;
var lollypops = 0;
var price = 10;

function updateCandies() {
  document.querySelector('.candies').innerHTML = candies;
}

function updateLollypops() {
  document.querySelector('.lollypops').innerHTML = lollypops;
}

function updateSpeed() {
  document.querySelector('.speed').innerHTML = getSpeed();
}

function getSpeed() {
  return Math.floor(lollypops / price);
}

document.querySelector('.create-candies').addEventListener('click', function() {
  candies++;
  updateCandies()
});

document.querySelector('.buy-lollypops').addEventListener('click', function() {
  if (candies > price) {
    lollypops++;
    candies -= price;
    updateLollypops();
    updateCandies()
    updateSpeed(getSpeed());
  }
});

setInterval(function () {
  candies += getSpeed();
  updateCandies()
  if (candies === 10000) {
    alert('WIN!');
  }
}, 1000);

