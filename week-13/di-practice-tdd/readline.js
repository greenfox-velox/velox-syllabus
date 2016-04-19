'use strict';

function FileReader(fileName, fs) {
  this.fileName = fileName;
  this.fs = fs;
}

FileReader.prototype.readLine = function(cb) {
  this.fs.readFile(this.fileName, function(err, content) {
    if (err) {
      return cb(err);
    }
    return cb(null, String(content).split('\n'));
  });
};

module.exports = FileReader;
