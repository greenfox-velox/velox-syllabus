'use strict';

const test = require('tape');
const supertest = require('supertest');

const createApp = require('./');


class FakeDate {
  toISOString() {
    return 'alma'
  }
}

const app = createApp(FakeDate);

test('app should be an express app', t => {
  t.equal(typeof app.listen, 'function');
  t.end();
});

test('it should have a /time endpoint', t => {
  supertest(app)
    .get('/time')
    .expect(200)
    .end((err, res) => {
      if (err) {
        return t.fail(err);
      }
      t.end();
    })
});

test('it should respond with json', t => {
  supertest(app)
    .get('/time')
    .expect('Content-Type', /json/)
    .end((err, res) => {
      if (err) {
        return t.fail(err);
      }
      t.end();
    })
});

test('it should respond with json', t => {
  supertest(app)
    .get('/time')
    .end((err, res) => {
      if (err) {
        return t.fail(err);
      }
      t.equal(typeof res.body.currentTime, 'string');
      t.end();
    })
});


test('it should respond with a date', t => {
  supertest(app)
    .get('/time')
    .end((err, res) => {
      if (err) {
        return t.fail(err);
      }
      t.equal(res.body.currentTime, 'alma');
      t.end();
    })
});

