# Callbacks

## Materials
 - https://www.youtube.com/watch?v=xHLd36QoS4k
 - https://www.youtube.com/watch?v=h0ZUpPiV1ac
 - https://www.youtube.com/watch?v=QRq2zMHlBz4
 - https://www.youtube.com/watch?v=U57kU311-nE
 - https://www.youtube.com/watch?v=YxWMxJONp7E
 - https://www.youtube.com/watch?v=JuyiVutx5vU
 - https://www.youtube.com/watch?v=y8xPMYwQ0U8
 - https://www.youtube.com/watch?v=1V7rpblmruw

## Workshop

### Read Write
```javascript
var fs = require('fs');

// synchronous

var rawContent = fs.readFileSync('apple.txt'); // Waits here and blocks everything
console.log(String(rawContent));

// asynchronous
fs.readFile('apple.txt', function(err, rawContent) {
  console.log(String(rawContent)); // jumps here later
});
// continues here before the console.log was called


```

#### Excercises

### XMLHttpRequest
```javascript



```

#### Excercises




### Candy game

gather 10.000 candies!
clicking the ‘Create candies’ button gives you 1 candy.
you can buy a lollipop for 100 candies by clicking the ‘Buy lollipop’ button.
10 lollipops generate 1 candy per second.
