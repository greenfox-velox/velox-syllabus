'use strict';

var fs = require('fs');

function wordCount(fileName, cb) {
  fs.readFile(fileName, function(err, content) {
    if (err) {
      return cb(err);
    }
    var count = String(content).split(/\s/g).length;
    cb(null, count);
  });
}

wordCount('zsomle.txt', function(err, c) {
  console.log(err, c);
});


