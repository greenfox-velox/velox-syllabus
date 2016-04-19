'use strict';

var probaRequest = new XMLHttpRequest();
console.log('probaRequest: ', probaRequest);


var gotResponse = function () {
  console.log('Request state: ', probaRequest.readyState);
  console.log('Response: ', probaRequest.response);
}
probaRequest.onreadystatechange = gotResponse;


var url = 'https://yoda.p.mashape.com/yoda';
var sentence = "I can make an XMLHttpRequest";
var urlWithParams = url + '?sentence=' + encodeURIComponent(sentence);
probaRequest.open('GET', urlWithParams);


var ACCESS_TOKEN = 'JNDzfN0Pz8mshV6DHISeFTRHJy00p1LvLoKjsnSUpz0krIeYGX';
probaRequest.setRequestHeader('X-Mashape-Key', ACCESS_TOKEN);


probaRequest.send();
