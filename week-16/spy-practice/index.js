'use strict';

var countWordsInHttp = require('./http-wc')();

countWordsInHttp(process.argv[2], function(err, count) {
  console.log(count);
});
