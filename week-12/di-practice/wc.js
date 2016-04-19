'use strict';

var fs = require('fs');

function WordCounter(fileName, fs) {
  this.fileName = fileName;
  this.fs = fs;
}

WordCounter.prototype.getCharacterCount = function(cb) {
  this.fs.readFile(this.fileName, function(err, content) {
    if (err) {
      return cb(err);
    }
    cb(null, String(content).length);
  });
};


var almaCount = new WordCounter('./alma.txt', fs);

module.exports = WordCounter;

almaCount.getCharacterCount(function(err, count) {
  console.log(count);
});
