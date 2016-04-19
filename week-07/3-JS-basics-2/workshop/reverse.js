// 1


function reverse(input) {
  var output = '';
  for (var i = input.length - 1; i >= 0; i--) {
    output += input[i];
  }
  return output;
}

console.log(reverse('kacsa'));


// recursive
function reverse2(input) {
  return reverseRecursive(input, input.length -1);
}

function reverseRecursive(input, i) {
  if (i < 0) {
    return '';
  } else {
    return input[i] + reverseRecursive(input, i - 1);
  }
}

console.log(reverse2('kacsa'));
