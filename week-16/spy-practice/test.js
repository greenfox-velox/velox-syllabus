'use strict';

var test = require('tape');
var sinon = require('sinon');
var httpWc = require('./http-wc');

test('it should create the counter', function(t) {
  var counter = httpWc();
  t.equal(typeof counter, 'function');
  t.end();
});

test('it should call the cb', function(t) {
  function fakeRequest(url, cb) {
    cb(null, {statusCode: 200}, 'teve');
  }

  var counter = httpWc(fakeRequest);
  counter('mamama', function(err, count) {
    t.equal(count, 1);
    t.end();
  });
});

test('it should call the cb', function(t) {
  function fakeRequest(url, cb) {
    cb(null, {statusCode: 200}, 'teve');
  }
  var spy = sinon.spy();

  var counter = httpWc(fakeRequest);
  counter('mamama', spy);
  t.equal(spy.called, true);
  t.end();
});

test('it should call the cb', function(t) {
  function fakeRequest(url, cb) {
    cb(null, {statusCode: 200}, 'teve');
  }
  var spy = sinon.spy();

  var counter = httpWc(fakeRequest);
  counter('mamama', spy);
  t.equal(spy.args[0][1], 1);
  t.end();
});

test('it should call the cb', function(t) {
  function fakeRequest(url, cb) {
    t.equal(url, 'mamama');
    t.end();
  }

  var counter = httpWc(fakeRequest);
  counter('mamama', function() {});
});

test('it should call the cb', function(t) {
  var spy = sinon.spy();

  var counter = httpWc(spy);
  counter('mamama', function() {});
  t.equal(spy.args[0][0], 'mamama');
  t.end();
});




