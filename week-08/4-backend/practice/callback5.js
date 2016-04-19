'use strict';

var fs = require('fs');

function countLetterP(callback) {
  fs.readFile('alma.txt', function(err, content) {
    var count = 0;
    var stringContent = String(content);
    for (var i = 0; i < stringContent.length; i++) {
      if (stringContent[i] === 'p') {
        count++;
      }
    }
    callback(count);
  });
}

countLetterP(function (count) {
  console.log(count); // -> 2
}); // in alma.txt (Pina)
