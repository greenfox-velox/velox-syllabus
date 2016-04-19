'use strict';

var request = require('request');

function httpWc(innerRequest) {
  innerRequest = innerRequest || request;
  function countWordsInHttp(url, cb) {
    innerRequest(url, function(err, response, body) {
      if (!err && response.statusCode === 200) {
        cb(null, body.split(/\s/).length);
      } else {
        cb(err);
      }
    }); 
  }

  return countWordsInHttp;
}

module.exports = httpWc;
