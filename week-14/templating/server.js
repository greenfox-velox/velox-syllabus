'use strict';


var express = require('express');

var app = express();

var count = 0;

app.set('view engine', 'ejs');

app.get('/', function(req, res) {
  count++;
  res.render('index', {count: count});
});

app.listen(3000);
