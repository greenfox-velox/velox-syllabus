'use strict';

function createMeal(connection) {
  function getAll(cb) {
    connection.query('SELECT * FROM meals;', cb);
  }

  return {
    getAll: getAll
  };
}


function createApp(connection) {
  var meal = createMeal(connection);
  app.get('/meals', function(req, res) {
    meal.getAll(function(err, meals) {
      res.json(meals);
    });
  });
}



var mysql = require('mysql');

var connection = mysql.connect({
  pass: 'secret'
});

var app = createApp(connection);
app.listen(3000);

tape(function(t) {
  var mockConnection = {
    query: function(sql, cb) {
      cb(null, [{}, {}, {}])
    }
  };
  var meal = createMeal(mockConnection);
  meal.getAll(function(err, meals) {
    t.equal(meals.length, 3);
    t.end();
  });
});


tape(function(t) {
  var mockConnection = {
    query: function(sql, cb) {
      cb(null, [{}, {}, {}])
    }
  };
  var app = createApp(mockConnection);
  supertest(app)
    .get('/meals')
    .end(function(err, res) {
       t.equal(res.body.length, 3);
       t.end();
    });
});
