'use strict';

var fs = require('fs');

function cesarDecode(fileName, cb) {
  fs.readFile(fileName, function(err, content) {
    if (err) {
      return cb(err);
    }
    var decodedString = String(content)
      .split('')
      .map(function(letter) {
        return String.fromCharCode(letter.charCodeAt() - 1); 
      }).join('');
    cb(null, decodedString);
  });
}

cesarDecode('encoded.txt', function(err, decodedFile) {
  console.log(decodedFile);
});

cesarDecode('blablalba', console.log);


