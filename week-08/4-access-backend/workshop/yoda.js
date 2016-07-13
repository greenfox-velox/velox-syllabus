var button = document.querySelector('button');
var textField = document.querySelector('input');
var resCont = document.querySelector('.result');

button.addEventListener('click', function() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'https://yoda.p.mashape.com/yoda?sentence=' + encodeURIComponent(textField.value));
  xhr.setRequestHeader('X-Mashape-Key', 'RjQ02YjhhKmsh2oPNmwkKK0oJ915p16Pku8jsnIqcYzOgxjLNV');
  xhr.onload = function() {
    resCont.innerHTML = xhr.response;
  };
  xhr.send();
});

for(var i = 5137; i < 5162; i++) {
  var xhr = new XMLHttpRequest();
  xhr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + i);
  xhr.onload = function() {
    console.log(i + ':' + xhr.status);
  };
  xhr.send()
}
