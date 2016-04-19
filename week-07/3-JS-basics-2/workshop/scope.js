'use strict';
var glob = 7;
var c = 8;

function printLocal() {
  var a = 123;
  c = 9;
  console.log(a);
  console.log(glob);
  console.log('local', c);
}

printLocal();
console.log('kunt', c);
// console.log(a); ERROR

function hurka() {
  for (var veres = 0; veres < 9; veres++) {
    console.log('Hurka');
  }
  console.log(veres);
  if (true) {
    var kecske = 'bleeee';
  }
  console.log(kecske);
}
hurka();
// console.log(veres); ERROR
