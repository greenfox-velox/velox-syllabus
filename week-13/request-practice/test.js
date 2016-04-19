'use strict';

var test = require('tape');
var supertest = require('supertest');

var createApp = require('./app');

function MockDate() {}
MockDate.prototype.toISOString = function() {
  return 'cica';
}

var app = createApp(MockDate);

test(function(t) {
  supertest(app)
    .get('/time')
    .expect(200)
    .end(function(err) {
      if (err) {
        t.fail(err);
      }
      t.end();
    })
});

test(function(t) {
  supertest(app)
    .get('/time')
    .end(function(err, res) {
      if (err) {
        t.fail(err);
      }
      t.equal(typeof res.body.currentTime, 'string');
      t.end();
    })
});

test(function(t) {
  supertest(app)
    .get('/time')
    .end(function(err, res) {
      if (err) {
        t.fail(err);
      }
      t.equal(res.body.currentTime, 'cica');
      t.end();
    })

})
