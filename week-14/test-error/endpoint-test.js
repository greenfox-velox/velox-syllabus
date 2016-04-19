'use strict';

var test = require('tape');
var supertest = require('supertest');

var createApp = require('./endpoint');

function instantiateApp(readFile) {
  var fakeFs = {
    readFile: readFile
  };
  return createApp(fakeFs);
}

function returnTest(err, cb) {
  cb(null, new Buffer('test'));
}

function returnKacsa(err, cb) {
  cb(null, new Buffer('kacsa'));
}

function returnError(err, cb) {
  cb(new Error('error'));
}

test('it should be an express app', function(t) {
  var app = instantiateApp(function() {});
  t.equal(typeof app.listen, 'function');
  t.end();
});

test('it should expose the /readfile endpoint', function(t) {
  var app = instantiateApp(returnTest);
  supertest(app)
    .get('/readfile')
    .expect(200)
    .end(function(err, res) {
      if (err) {
        t.fail(err);
      }
      t.end();
    });
});

test('it should response a JSON', function(t) {
  var app = instantiateApp(returnTest);
  supertest(app)
    .get('/readfile')
    .expect('Content-Type', /json/)
    .end(function(err, res) {
      if (err) {
        t.fail(err);
      }
      t.end();
    });
});

test('it should response the file content', function(t) {
  var app = instantiateApp(returnTest);
  supertest(app)
    .get('/readfile')
    .end(function(err, res) {
      if (err) {
        t.fail(err);
      }
      t.deepEqual(res.body, {content: 'test'});
      t.end();
    });
});

test('it should response different file content', function(t) {
  var app = instantiateApp(returnKacsa);
  supertest(app)
    .get('/readfile')
    .end(function(err, res) {
      if (err) {
        t.fail(err);
      }
      t.deepEqual(res.body, {content: 'kacsa'});
      t.end();
    });
});

test('it should response 500 on error', function(t) {
  var app = instantiateApp(returnError);
  supertest(app)
    .get('/readfile')
    .expect(500)
    .end(function(err, res) {
      if (err) {
        t.fail(err);
      }
      t.end();
    });
});

test('it should response 500 on error', function(t) {
  var app = instantiateApp(returnError);
  supertest(app)
    .get('/readfile')
    .expect(500)
    .end(function(err, res) {
      if (err) {
        t.fail(err);
      }
      t.deepEqual(res.body, {status: 'fail'});
      t.end();
    });
});

test('it should read the data.txt file', function(t) {
  var app = instantiateApp(function(fileName, cb) {
    t.equal(fileName, 'data.txt');
    cb(null, new Buffer('data'));
  });
  supertest(app)
    .get('/readfile')
    .end(function(err, res) {
      if (err) {
        t.fail(err);
      }
      t.end();
    });
});


