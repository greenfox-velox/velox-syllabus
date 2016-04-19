'use strict';

var tape = require('tape');
var ImageStore = require('./image-store');

tape(function(t) {
  t.equal(typeof new ImageStore([]), 'object');

  var store = createStore();
  t.equal(store.getCurrentSrc(), 'test.jpg');

  var store = createStore(['test2.jpg']);
  t.equal(store.getCurrentSrc(), 'test2.jpg');

  var store = createStore();
  store.next();
  t.equal(store.getCurrentSrc(), 'test2.jpg');

  var store = createStore();
  store.next();
  store.next();
  t.equal(store.getCurrentSrc(), 'test.jpg');

  var store = createStore();
  store.next();
  store.prev();
  t.equal(store.getCurrentSrc(), 'test.jpg');

  var store = createStore();
  store.prev();
  t.equal(store.getCurrentSrc(), 'test2.jpg');

  t.end();
});

function createStore(images) {
  if (images === undefined) {
    images = ['test.jpg', 'test2.jpg'];
  }
  return new ImageStore(images);
}
