'use strict';

var a = 2;

if (a === 2) {
  console.log(a);
}

if (a === 2) {
  console.log('two');
} else {
  console.log('other');
}

if (a === 1) {
  console.log('one');
} else if (a === 2) {
  console.log('two');
} else {
  console.log('a lot');
}

/* eslint-disable no-empty */
if (a === 1) {

} else {
  console.log('not one');
}
/* eslint-enable no-empty */
