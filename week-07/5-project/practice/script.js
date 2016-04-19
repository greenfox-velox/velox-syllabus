'use strict';

var buttons = document.querySelector('.buttons');

buttons.addEventListener('click', function(event) {
  console.log(event.target);
  alert('JUUHUUU a button 1');
});
