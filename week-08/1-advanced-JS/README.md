# Advanced JS

## Materials
 - https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/this
 - https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/prototype
 - https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/var
 - http://javascript.info/tutorial/arguments
 - https://www.youtube.com/watch?v=IGqGqlyIcg8
 - https://www.youtube.com/watch?v=riDVvXZ_Kb4
 - https://www.youtube.com/watch?v=BMUiFMZr7vk
 - https://www.youtube.com/watch?v=bCqtb-Z5YGQ
 - https://www.youtube.com/watch?v=Wl98eZpkp-c
### If you are brave:
 - https://www.youtube.com/watch?v=Wl98eZpkp-c

## Assigment review
 - Higher order functions
 - reduce
 - Hoisting
 - function scope
 - this
 - arguments
 - prototype
 - casting
 - `isPrototypeOf`
### Talk about
 - `||`, `$$`
 - tape
 - modules

## Workshop
Please write unit tests for all your objects and functions
In your working directory:
```bash
npm init
npm install tape
```

### and, or
```javascript
var fruit = 'apple' || true;
console.log(fruit); // apple

var string = '' && 'monkey';
console.log(string); // ''

var obj = {prop: 12};

console.log(obj && obj.prop); // 12
```

#### Excercises
 - [01.js](workshop/01.js)
 - [02.js](workshop/02.js)

### Prototype
```javascript
function Car(km) {
  this.km = km;
}

Car.prototype.ride = function(km) {
  this.km += km;
}

var volvo = new Car(80000);
volvo.ride(120);
console.log(volvo.km); // 801200


var food = {name: 'food-name', calories: 0};

var pasta = Object.create(food);
pasta.name = 'pasta';
console.log(pasta.calories); // 0
pasta.calories = 540;
console.log(pasta.calories); // 540
console.log(food.calories); // 0

var fish = Object.create(food);
fish.name = 'fish';
console.log(fish.calories); // 0
food.calories = 12;
console.log(fish.calories); // 12
console.log(food.calories); // 12
```

#### Excercises
For the fourh excercise you should check out:
https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Date

 - [03.js](workshop/03.js)
 - [04.js](workshop/04.js)

### reduce
```javascript
var numbers = [1, 5, 6, 2, 8];

var sum = numbers.reduce(function(accumulator, element) {
  return accumulator + element;
}, 0);

console.log(sum); // 22
```
