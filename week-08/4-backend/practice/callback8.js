'use strict';

var fs = require('fs');


fs.readFile('alma.txt', almaRead);

function almaRead(err, almaContent) {
  fs.readFile('korte.txt', function (err, korteContent) {
    console.log(almaContent + korteContent);
  });
}
