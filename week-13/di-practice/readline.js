'use strict';

 var fs = require('fs');

function FileReader(fileName, newFs) {
  this.fileName = fileName;
  this.fs = newFs || fs;
}


FileReader.prototype.readLines = function(cb) {
  this.fs.readFile(this.fileName, function(err, content) {
    if (err) {
      return cb(err);
    }
    cb(null, String(content).split('\n'));
  });
};

module.exports = FileReader;
