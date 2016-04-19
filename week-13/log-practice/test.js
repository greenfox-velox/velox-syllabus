'use strict';

var test = require('tape');

var createLogger = require('./loginfo');

test(function(t) {
  var logger = createLogger();
  t.equal(typeof logger.logInfo, 'function')
  t.end();
});

test(function(t) {
  function fakeConsoleLog(text) {
    t.equal(text, 'INFO kacsa datum');
    t.end();
  }
  function FakeDate() {}
  FakeDate.prototype.toISOString = function() {
    return 'datum';
  };
  var logger = 
    createLogger(fakeConsoleLog, FakeDate);
  logger.logInfo('kacsa');
});

