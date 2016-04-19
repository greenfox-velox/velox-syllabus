'use strict';

var express = require('express');

function createApp(Date) {
  var app = express();
  app.get('/time', function(reg, res) {
    var date = new Date();
    res.json({
      currentTime: date.toISOString()
    });
  });
  return app;
}

module.exports = createApp;
