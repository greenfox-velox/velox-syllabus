'use strict';

var numbers = [5, 7, 9, 11, 13, 12];

var i = 0;
while (i < numbers.length) {
  if (numbers[i] % 3 !== 0) {
    console.log('nope');
  } else {
    console.log(numbers[i]);
    break;
  }
  i += 1;
}
