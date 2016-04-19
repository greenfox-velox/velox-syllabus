'use strict';

function textMultiply(text, number) {
  var output = '';
  for (var i = 0; i < number; i++) {
    output += text;
  }
  return output;
}

function textMultiply(text, number) {
    return number ? text + textMultiply(text, number - 1) : '';
}

console.log(textMultiply('alma', 3)); // almaalmaalma
