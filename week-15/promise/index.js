'use strict';

function giveAnAppleOneSecond(cb) {
  setTimeout(function() {
    cb('apple');
  }, 1000);
}

giveAnAppleOneSecond(function(a) {
  console.log(a);
});







function giveAnAppleOneSecondPromise() {
  return new Promise(function(resolve) {
    setTimeout(function() {
      resolve('apple');
    }, 1000);
  });
}


var promise = giveAnAppleOneSecondPromise();
promise.then(function(a) {
  return a + 'tree';
}).then(function(b) {
  console.log(b);
});

