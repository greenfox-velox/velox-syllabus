'use strict';

var probaRequest = new XMLHttpRequest();
console.log('probaRequest: ', probaRequest);

var url = 'http://www.greenfoxacademy.com/';
probaRequest.open('GET', url);
probaRequest.send();
