'use strict';

var test = require('tape');
var FileReader = require('./readline');

test('filereader', function(t) {
  var fs = {
    readFile: function(name, cb) {
      cb(null, new Buffer('alma'));
    }
  };

  var reader = new FileReader('test.txt', fs);
  
  reader.readLines(function(err, lines) {
    t.deepEqual(lines, ['alma']);
    t.end();
  });
});
