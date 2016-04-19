'use strict';

/*
var button = document.querySelector('button');

button.addEventListener('click', function () {
  shout('kacsa');
});

function shout(word) {
  console.log('AJAJAJAJAJJA');
  console.log('AJAJAJAJAJJA');
  console.log('AJAJAJAJAJJA', word);
  console.log('AJAJAJAJAJJA');
  console.log('AJAJAJAJAJJA');
  console.log('AJAJAJAJAJJA');
}

*/

var human = {
  word: ['Kacsa', 'Macska', 'Mammlasz'],
  name: 'Tibbor',
  speak: speak,
  say: say
};


function speak() {
  var _this = this;
  this.word.forEach(this.say);
}

function say(w) {
  console.log('I am ' + _this.name);
  console.log('Bla-bla-bla ' + w);
}


human.speak();














