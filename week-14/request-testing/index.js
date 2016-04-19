'use strict';

const express = require('express');

function createApp(InnerDate) {
  InnerDate = InnerDate || Date;

  const app = express();
  app.get('/time', (req, res) => {
    const date = new InnerDate();
    res.json({
      currentTime: date.toISOString()
    });
  });
  
  return app;
}


module.exports = createApp;
