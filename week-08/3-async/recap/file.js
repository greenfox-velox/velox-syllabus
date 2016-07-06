'use strict';

var fs = require('fs');

fs.readFile('alma.txt', function(err, c) {
  console.log(String(c));
  fs.writeFile('korte.txt',
               String(c) + 'beka',
               function(err, c) {
    console.log('end');
  });
});
console.log('after');

