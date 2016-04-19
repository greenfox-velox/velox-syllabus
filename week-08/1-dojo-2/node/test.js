'use strict';

var arabic2roman = require('./kata');
var tape = require('tape');

tape('roman converter', function(t) {
  t.equal(arabic2roman(0), '');

  t.end();
});
