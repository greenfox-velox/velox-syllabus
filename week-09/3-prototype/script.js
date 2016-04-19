'use strict';

var buttons = document.querySelectorAll('button');

for (var i = 0; i < 5; i++) {
  (function(i) {
    buttons[i].addEventListener('click', function() {
      alert(i + 1);
    });
  })(i);
}
