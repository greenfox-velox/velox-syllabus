'use strict';

var test = require('tape');
var FileReader = require('./readline');

test('filereader exists', function(t) {
  t.equal(typeof FileReader, 'function');
  t.end();
});

test('readLine exists', function(t) {
  var reader = new FileReader('alma.txt');
  t.equal(typeof reader.readLine, 'function');
  t.end();
});

test('readLine passes the file', function(t) {
  var fs = {
    readFile: function(fileName, cb) {
      t.equal(fileName, 'alma.txt');
      t.end();
    } 
  };

  var reader = new FileReader('alma.txt', fs);
  reader.readLine(function() {});
});

test('readLine passes the file', function(t) {
  var fs = {
    readFile: function(fileName, cb) {
      cb(null, new Buffer(''));
    } 
  };

  var reader = new FileReader('alma.txt', fs);
  reader.readLine(function(err, lines) {
    t.deepEqual(lines, ['']);
    t.end();
  });
});

test('readLine passes the file', function(t) {
  var fs = {
    readFile: function(fileName, cb) {
      cb(null, new Buffer('alma'));
    } 
  };

  var reader = new FileReader('alma.txt', fs);
  reader.readLine(function(err, lines) {
    t.deepEqual(lines, ['alma']);
    t.end();
  });
});

test('readLine passes the file', function(t) {
  var fs = {
    readFile: function(fileName, cb) {
      cb(null, new Buffer('alma\nkorte'));
    } 
  };

  var reader = new FileReader('alma.txt', fs);
  reader.readLine(function(err, lines) {
    t.deepEqual(lines, ['alma', 'korte']);
    t.end();
  });
});

test('readLine passes the file', function(t) {
  var fs = {
    readFile: function(fileName, cb) {
      cb('PARA');
    } 
  };

  var reader = new FileReader('alma.txt', fs);
  reader.readLine(function(err, lines) {
    t.deepEqual(err, 'PARA');
    t.end();
  });
});


