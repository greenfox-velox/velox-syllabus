'use strict';

var express = require('express');

var app = express();


app.get('/apple', function(req, res) {
  console.log('apple');
  setTimeout(function(items) {
    res.send('<h1>kacsa</h1>');
  }, 1000);
});

app.listen(3000);

