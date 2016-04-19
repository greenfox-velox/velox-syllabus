'use strict';

var tape = require('tape');

var arabic2roman = require('./kata');

tape('roman converter', function(t) {
  t.equal(arabic2roman(0), '');

  t.end();
});
