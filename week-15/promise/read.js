'use strict';

var fsp = require('fs-promise');

fsp.readFile('alma.txt').then(function(content) {
  console.log(String(content));
});

