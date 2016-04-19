'use strict';

var FileReader = require('./readline');

var fileReader = new FileReader('./alma.txt');

fileReader.readLines(function(err, lines) {
  console.log(lines);
});
