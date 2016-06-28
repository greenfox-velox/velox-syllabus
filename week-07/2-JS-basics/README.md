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
console.log(['apple', 'pear', 'melon'].indexOf('pear')); // 1

['apple', 'pear', 'melon'].forEach(function(e) {
  console.log(e);
});


var triples = [1, 2, 3, 4, 5].map(function(e) {
  return e * 3;
});
console.log(triples); // [3, 6, 9, 12, 15]

var evens = [1, 2, 3, 4, 5].filter(function(e) {
  return e % 2 === 0;
});
console.log(evens); // [2, 4]

var isAllEven = [2, 6, 14, 5, 4].every(function(e) {
  return e % 2 === 0;
});
console.log(isAllEven); // false

var isAnyEven = [2, 6, 14, 5, 4].some(function(e) {
  return e % 2 === 0;
});
console.log(isAnyEven); // true

var letters = 'apple'.split('');
console.log(letters); // ['a', 'p', 'p', 'l', 'e']
```

#### Excercises
try to avoid using for and while (except for the prime detection)
 - [04.js](workshop/04.js)
 - [05.js](workshop/05.js)
 - [06.js](workshop/06.js)
 - [07.js](workshop/07.js)


### Object literal
```javascript
var student = {
  name: 'Darth Vader',
  age: 42,
  isForceSensitive: true
};

console.log(student.name); // 'Darth Vader'
var key = 'age'
console.log(student[key]); // 42
Object.keys(student); // ['name', 'age', 'isForceSensitive']
```

#### Excercises
 - [08.js](workshop/08.js)
 - [09.js](workshop/09.js)

### method and this
```javascript
var car = {
  km: 120000,
  ride: function(km) {
    this.km += km;
  }
};

car.ride(200);
console.log(car.km); // 120200
```

#### Excercises
 - [10.js](workshop/10.js)

### Constructor
```javascript
function Car(startKm) {
  this.km = startKm;
  this.ride = function(km) {
    this.km += km;
  }
}

var car = new Car(120000);

car.ride(200);
console.log(car.km); // 120200
```
#### Excercises
 - [11.js](workshop/11.js)

### Strings
[documentation](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String)
#### Converter object
Create an object that has several converter methods:
 - `float2string(num)` it should convert a float number to a string, for example 12.24 -> '12.24'
 - `string2float(str)` it should convert a string to a float number, for example '12.24' -> 12.24
 - `int2roman(number)` it should convert an int number to a roman number as a string, for example 12 -> 'XII'
 - `roman2int(number)` it should convert a roman number as a string to an int, for example 'XII' -> 12
please try to avoid using the built in conversion methods

### Math
[documentation](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Math)

#### Excercises
##### Cows and Bulls
Create a class what is capable of playing exactly one game of Cows and Bulls (CAB). The player have to guess a 4 digit number. For every digit that the player guessed correctly in the correct place, they have a “cow”. For every digit the player guessed correctly in the wrong place is a “bull.”

 - The CAB object should have a random 4 digit number, which is the goal to guess.
 - The CAB object should have a state where the game state is stored (playing, finished).
 - The CAB object should have a counter where it counts the guesses.
 - The CAB object should have a guess method, which returns a string of the guess result
 - All methods, including constructor should be tested

