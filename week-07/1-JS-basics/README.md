# Monday - JavaScript Basics

## Materials for this day
- https://www.youtube.com/playlist?list=PL4cUxeGkcC9i9Ae2D9Ee1RvylH38dKuET

### Assignment review
 - Comments
 - Types
   - number
   - string
   - boolean
   - null
   - undefined
   - array
 - Operators
   - arithmetric
   - logical
   - comparison
   - assignment
   - typeof
 - Control structures
   - `if`
   - `while`
   - `for`
   - `break`
   - `continue`
 - Functions
   - definition
   - invocation
   - arguments
   - return value

## Required installs
- Please install Node.js v4.4.6
https://nodejs.org/en/download/

## JavaScript Reference https://developer.mozilla.org/en-US/docs/Web/JavaScript

## Workshop

### Hello World
```javascript
'use strict';

console.log('Hello world')
```

### Comments
```javascript
'use strict';

// single line comment

/*
  multi line
  comment block
*/
```

### Numbers
```javascript
'use strict';

1;
0;
-1;
12.23;
12341234123412341234;
1e3;
0b11;
011;
0x11;

1 + 2;
2 - 1;
4 * 3;
2 / 3;
5 & 3;
1 % 2;
(1 + 3) * 4;

1 / 0;
-1 / 0;
0 / 0;
Infinity;
-Infinity;
NaN;
Infinity + 123;
NaN / 12;
Infinity - Infinity;
NaN * NaN;
```

### Variables
```javascript
'use strict';

// Declare variable
var a;

// Define variable
a = 123;

// Re-define variable
a = 432;

// use variable in expression
a = a + 1;

// Define undeclared variable (try with and without use strict)
b = 2;

// Assignment operators
a = 3;
a += 1;
a -= 2;
a *= 6;
a /= 2;
a %= 2;

// Increment operators
a++;
++a;
a--;
--a;

a = 1;
console.log(a);
console.log(a++);
console.log(a);

a = 1;
console.log(a);
console.log(++a);
console.log(a);

// use camel case variables
var minutesSinceYestreday;

// undefined
var c;
console.log(c);
```

#### Excercises
- [01.js](workshop/01.js)
- [02.js](workshop/02.js)
- [03.js](workshop/03.js)
- [04.js](workshop/04.js)
- [05.js](workshop/05.js)
- [06.js](workshop/06.js)


### Boolean
```javascript
'use strict';

var a = 2;
a === 2;
true;
false;

1 < 2;
1 > 2;
1 >= 2;
1 <= 2;
1 === 2;
1 !== 2;
true || false;
true && false;
!true;

typeof 1;
typeof 1 === 1;
```

#### Excercises
- [07.js](workshop/07.js)
- [08.js](workshop/08.js)
- [09.js](workshop/09.js)
- [10.js](workshop/10.js)
- [11.js](workshop/11.js)

### Strings
```javascript
'use strict';

"apple";
"";
typeof "apple";

'He is sooo "smart"...';
'don\'t';

'apple' - 'tree'; // NaN
'apple' * 3; // NaN
'apple' + 'tree'; // appletree
'apple' + 3; // automated casting
10 + "alma";
10 + "3";

"alma".length;
"alma"[1];
parseInt("123", 10);
```

#### Excercises
- [12.js](workshop/12.js)
- [13.js](workshop/13.js)
- [14.js](workshop/14.js)
- [15.js](workshop/15.js)

### Arrays
```javascript
'use strict';

[1, 2, 3];
[];
typeof [1, 2];
[1, 2, 3].length;
var arr = [1, 2, 3];
arr[0];
```

#### Excercises
- [16.js](workshop/16.js)
- [17.js](workshop/17.js)
- [18.js](workshop/18.js)
- [19.js](workshop/19.js)
- [20.js](workshop/20.js)

### Nothings
```javascript
'use strict';

undefined;
null;
NaN;

null !== undefined;
NaN !== undefined;
null !== NaN;

null == undefined;

typeof undefined; // 'undefined'
typeof null; // 'object'
typeof NaN; // 'number' :'D

var alma;
alma; // undefined
alma + 1; // NaN
alma = null; // null
```

### If
```javascript
'use strict';

if (a === 2) {
  console.log(a);
}


if (a === 2) {
  console.log("two");
} else {
  console.log("other");
}


if (a === 1) {
  console.log("one");
} else if (a === 2) {
  console.log("two");
} else {
  console.log("a lot");
}

if (a === 1) {

} else {
  console.log("not one");
}
```

#### Excercises
- [21.js](workshop/21.js)
- [22.js](workshop/22.js)
- [23.js](workshop/23.js)
- [24.js](workshop/24.js)
- [25.js](workshop/25.js)
- [26.js](workshop/26.js)
- [27.js](workshop/27.js)
- [28.js](workshop/28.js)
- [29.js](workshop/29.js)
- [30.js](workshop/30.js)


### While
```javascript
'use strict';

var a = 0;
while (a < 5) {
  a += 1;
  console.log(a);
}
```

#### Excercises
- [31.js](workshop/31.js)
- [32.js](workshop/32.js)
- [33.js](workshop/33.js)
- [34.js](workshop/34.js)
- [35.js](workshop/35.js)
- [36.js](workshop/36.js)
- [37.js](workshop/37.js)

### For
```javascript
'use strict';

for (var i = 0; i < 4; i++) {
  console.log(i);
}

var array = [1, 2, 3, 4];
for (var j = 0; j < array.length; j++) {
  console.log(array[j]);
}
```

#### Excercises
- redo the While excercises with for
- FizzBuzz [38.js](workshop/38.js)

### break & continue
```javascript
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
```

```javascript
'use strict';

var numbers = [5, 7, 9, 11, 13, 12];

var i = 0;
while (i < numbers.length) {  
  if (numbers[i] % 3 != 0) {
    continue;
  } else {  
    console.log(numbers[i]);
  }
  i += 1;
 }
}
```

### Functions
```javascript
'use strict';

function add(a, b) {
  return a + b;
}

console.log(add(1, 2));
```

#### Excercises
 - [39.js](workshop/39.js)
 - [40.js](workshop/40.js)
 - [41.js](workshop/41.js)
 - [42.js](workshop/42.js)
 - [43.js](workshop/43.js)
 - [44.js](workshop/44.js)
 - [45.js](workshop/45.js)


### NPM, packages, eslint
- initialize a node project in today's working directory
- install eslint
- initialize eslint based on a popular style guide / AirBnB
- install 3 missing dependencies causing all the ugly red error messages
- install atom linter-eslint package
- profit
```
npm init
npm install -g eslint
eslint --init
npm i --save-dev eslint-plugin-import@^1.7.0 eslint-plugin-import@^1.7.0 eslint-plugin-jsx-a11y@^1.2.0
```

### Bonus Excercises
- rewrite the python command line [recursion exercises](../../week-04/4-recursion) in JavaScript
- watch https://www.destroyallsoftware.com/talks/wat and reproduce the JavaScript examples
