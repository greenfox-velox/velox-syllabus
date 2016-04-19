'use strict';

var test = require('tape');
var WordCounter = require('./wc');


test('existance', function(t) {
  t.equal(typeof WordCounter, 'function');
  t.end();
});

test('robika in da file', function(t) {
  var fakeFs = {
    readFile: function(fileName, cb) {
      cb(null, new Buffer('robika'));
    }
  };
  var testCounter = new WordCounter('teve', fakeFs);
  testCounter.getCharacterCount(function(err, count) {
    t.equal(count, 6);
    t.end();
  });
});

test('error \'bout da file', function(t) {
  var fakeFs = {
    readFile: function(fileName, cb) {
      cb('ACHTUNG!!');
    }
  };
  var testCounter = new WordCounter('teve', fakeFs);
  testCounter.getCharacterCount(function(err, count) {
    t.equal(count, undefined);
    t.ok(err);
    t.end();
  });
});

test('error \'bout da file', function(t) {
  var fakeFs = {
    readFile: function(fileName, cb) {
      t.equal(fileName, 'teve');
      t.end();
      cb(null, null);
    }
  };
  var testCounter = new WordCounter('teve', fakeFs);
  testCounter.getCharacterCount(function() {});
});
