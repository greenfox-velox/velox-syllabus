'use strict';

var express = require('express');
var bodyParser = require("body-parser");
var Meal = require('./meal');

var mysql = require('mysql');

var connection = mysql.createConnection({
  host : 'localhost',
  user : 'root',
  password : process.env.MYSQL_PASS || '',
  database : 'calorie'
});

connection.connect();

var meal = new Meal(connection);

var app = express();

app.use(express.static('public'));
app.use(bodyParser.json());

app.listen(3000);

app.post('/meals', function (req, res) {
  meal.add(req.body, function(err, result) {
  	res.json({
    	status: 'ok'
  	});	
  });
});

app.get('/meals', function (req, res) {
  meal.getAll(function(err, meals) {
    res.json(meals);
  });
});

app.delete('/meals/:id', function (req, res) {
  meal.del(req.params.id, function(err, result) {
    if (err) {
      res.json({status: 'not exists'});
    } else {
      res.json({status: 'ok'});
    }
  });
});
