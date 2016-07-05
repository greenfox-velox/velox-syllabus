'use strict';

var isEnd = false;
setTimeout(function() {
  console.log('JEJ!');
  isEnd = true;
}, 0);

function end() {
  console.log('END!');
  console.log('END2!');
}

end();
