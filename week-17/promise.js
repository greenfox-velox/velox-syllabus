'use strict';

var p1 = new Promise(function(resolve, reject) {
  setTimeout(function() {
    resolve(4);
  }, 4000);
});
var p2 = new Promise(function(resolve, reject) {
  setTimeout(function() {
    resolve(5);
  }, 5000);
});

Promise.all([p1, p2]).then(console.log);


Promise.all([1, 2, 3, 4].map((i) => new Promise((resolve) => resolve(i)))).then(console.log);
