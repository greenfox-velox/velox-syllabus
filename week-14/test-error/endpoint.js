'use strict';

var express = require('express');

function createApp(fs) {
  var app = express();

  app.get('/readfile', function(req, res) {
    fs.readFile('data.txt',
      function(err, content) {
        if (err) {
          return res.status(500).json({status: 'fail'});
        }
        res.json({content: String(content)});
      });
  });

  return app;
}

module.exports = createApp;
