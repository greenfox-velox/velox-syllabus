'use strict';

var fs = require('fs');

fs.readFile('korte.txt', function(err, content) {
  if (err) {
    console.log('Para volt');
  } else {
    console.log(content);
  }
})
