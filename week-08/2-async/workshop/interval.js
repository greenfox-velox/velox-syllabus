'use strict';
var count = 0;
var interval = setInterval(function() {
  count++;
  console.log('Je-Je-Jee!', count);
}, 500);

setTimeout(function() {
  console.log('BOOM!');
  clearInterval(interval);
}, 5000);

setTimeout(function() {
  for (var i = 0; i < 1234123421; i++) {

  }
}, 2000);
