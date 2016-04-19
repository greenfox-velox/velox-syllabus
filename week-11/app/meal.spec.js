'use strict';

var tape = require('tape');

var Meal = require('./meal');

tape('query return', function(t) {
  var connection = {};
  connection.query = function(query, cb) {
    cb(null, [{}]);
  };
  var meal = new Meal(connection);
  meal.getAll(function(err, meals) {
    t.ok(meals.length > 0);
    t.end();
  });
});

tape('query string', function(t) {
  var connection = {};
  connection.query = function(query, cb) {
    t.equal(query, 'SELECT * FROM meal');
    t.end();
  };
  var meal = new Meal(connection);
  meal.getAll();
});

// same thing with a spy
var sinon = require('sinon');

tape(function(t) {
  var connection = {};
  connection.query = sinon.spy(function(query, cb) {
    cb(null, [{}]);
  });
  var meal = new Meal(connection);
  meal.getAll(function(err, meals) {
    t.ok(meals.length > 0);
  });
  t.equal(connection.query.args[0][0], 'SELECT * FROM meal');
  t.end();
});

