'use strict';

var fs = require('fs');

function readAlmaTxt(callback) {
  fs.readFile('alma.txt', function(err, content) {
    var output = String(content);
    callback(output);
  });
}

readAlmaTxt(function(content) {
  console.log(content);
});
