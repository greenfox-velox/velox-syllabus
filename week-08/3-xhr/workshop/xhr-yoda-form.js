'use strict';


var probaRequest;

var createRequest = function (url, callback) {

  probaRequest = new XMLHttpRequest();
  console.log('probaRequest: ', probaRequest);

  probaRequest.onreadystatechange = callback;
  probaRequest.open('GET', url);

  var ACCESS_TOKEN = 'JNDzfN0Pz8mshV6DHISeFTRHJy00p1LvLoKjsnSUpz0krIeYGX';
  probaRequest.setRequestHeader('X-Mashape-Key', ACCESS_TOKEN);

  probaRequest.send();
}



var yodaInput = document.querySelector('.yoda-input');
var yodaButton = document.querySelector('.convert-button');
var yodaResult = document.querySelector('.result');

var onConvertClick = function () {
  var url = 'https://yoda.p.mashape.com/yoda';
  var sentence = yodaInput.value;
  var urlWithParams = url + '?sentence=' + encodeURIComponent(sentence);

  var callbackFunction = function () {
    console.log('Request state: ', probaRequest.readyState);
    console.log('Response: ', probaRequest.response);
    if (probaRequest.readyState === XMLHttpRequest.DONE) {
      console.log('Request done!');
      yodaResult.innerText = probaRequest.response;
    }
  };

  createRequest(urlWithParams, callbackFunction);
}

yodaButton.addEventListener('click', onConvertClick);
