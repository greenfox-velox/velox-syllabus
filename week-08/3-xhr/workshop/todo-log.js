'use strict';

var probaRequest = new XMLHttpRequest();
console.log('probaRequest: ', probaRequest);

var gotResponse = function () {
  console.log('Request state: ', probaRequest.readyState);
  if (probaRequest.readyState === XMLHttpRequest.DONE) {
    console.log('Request done!');
    console.log('Response: ', JSON.parse(probaRequest.response));
  }
}
probaRequest.onreadystatechange = gotResponse;

var URL = 'https://mysterious-dusk-8248.herokuapp.com/todos';

probaRequest.open('GET', URL);

probaRequest.send();

// probaRequest.open('POST', URL);
// probaRequest.setRequestHeader('Content-Type', 'application/json');
//
// probaRequest.send(JSON.stringify({text: 'Create todos'}));
