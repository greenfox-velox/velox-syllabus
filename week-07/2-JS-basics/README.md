# Tuesday - Arrays and Objects 

## Materials for this day
 - https://www.youtube.com/watch?v=lK42xIMcA0Y
 - https://www.youtube.com/watch?v=xHLd36QoS4k
 - http://javascript.info/tutorial/functions-declarations-and-expressions
 - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
   - till the properties chapter
 - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat
 - http://colintoh.com/blog/5-array-methods-that-you-should-use-today
   - expect Demethodizing chapter
 - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every
 - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some
 - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects 
   - except getters and setters chapter
 - https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/switch

### Assignment review
 - switch
 - function expressions
   - function as variable
   - function as parameter
   - anonymus function
 - array methods
   - `push`
   - `pop`
   - `shift`
   - `unshift`
   - `indexOf`
   - `slice`
   - `splice`
   - `concat`
   - `forEach`
   - `filter`
   - `map`
   - `every`
   - `some`
 - object
   - literal
   - creating, adding, modifying, accessing and deleting properties
   - methods
   - `this`
   - constructor function

## Workshop
### Switch
```javascript
var number = 1;

switch (number) {
  case 0:
    console.log('zero');
    break;
  case 1:
    console.log('one');
    break;
  case 2:
    console.log('two');
    break;
  default:
    console.log('many');
    break;
}
```

#### Excercise
 - [01.js](workshop/01.js)

### functions as variables
```javascript
'use strict'

function greet(name) {
  console.log('Hi ' + name + '!');
}

var myGreet = greet;
myGreet('Steve'); // "Hi Steve!"
```
```javascript
'use strict';

var add = function (a, b) {
  return a + b;
};

console.log(add(1, 2)); // 3
```
```javascript
function run(func, arg) {
  func(arg);
}

function greet(name) {
  console.log('Hi ' + name + '!');
}

run(greet, 'Steve'); // "Hi Steve!"
```
#### Excercises
 - [02.js](workshop/02.js)
 - [03.js](workshop/03.js)


### Array methods
```javascript

```


### Object literal
```javascript

```

### method and this
```javascript

```

### Constructor
```javascript
```
#### Excercises
