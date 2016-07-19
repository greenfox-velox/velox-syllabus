
'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var mysql = require('mysql');
var meal = require('meal');

var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'start',
  database: 'dbcalorie',
});

var myMeal = meal(con);

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(express.static('client'))

app.post('/meals', function(req, res){
  var meal = {
    name: req.body.name,
    calories: req.body.calories,
    date: req.body.date
  }
  var callback = function (result) {
    console.log(result);
    res.json({"status": "ok"});
  }
  myMeal.addMeal(meal, callback);
});

app.listen(3000);
