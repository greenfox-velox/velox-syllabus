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
 - https://www.youtube.com/watch?v=qN0dkXj7jc0

## Assignment review
 - setTimeout
 - setInterval
 - clearTimeout
 - clearInterval
 - blocking / non blocking
 - fs.readFile
 - fs.writeFile
 - AJAX

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
Please dont use the Sync versions of the methods
 - [01.js](workshop/01.js)
 - [02.js](workshop/02.js)
 - [03.js](workshop/03.js)
 - [04.js](workshop/04.js)
 - [05.js](workshop/05.js)

### XMLHttpRequest
```javascript
var xhr = new XMLHttpRequest();                                              
xhr.onload = function() {                                                    
  console.log(xhr.response);                                                 
};                                                                             
xhr.open('GET', 'http://calapi.inadiutorium.cz/api/v0/en/calendars/default/2015/6/27')
xhr.send();  
```

#### Date page
create a page:
it should have a button that fires a request to the calendar api described [here](http://calapi.inadiutorium.cz/)
if it responses, it should wirte the current work day and how many celebrations are on that day


### setTimeout setInterval
```javascript

```


#### Candy game

gather 10.000 candies!
clicking the ‘Create candies’ button gives you 1 candy.
you can buy a lollipop for 100 candies by clicking the ‘Buy lollipop’ button.
10 lollipops generate 1 candy per second.
