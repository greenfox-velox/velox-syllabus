'use strict';

function runIn5Seconds(callback) {
  setTimeout(callback, 5000);
}


runIn5Seconds(function() {
  console.log('jeej');
});
