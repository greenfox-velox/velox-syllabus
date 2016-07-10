# Backend in Node.js

## Materials
 - https://www.youtube.com/watch?v=qSAze9b0wrY
 - https://www.youtube.com/watch?v=lm86czWdrk0
 - https://www.youtube.com/watch?v=kQ1j0rEI7EI
 - https://www.youtube.com/watch?v=_eRwjuIDJ2Y
 - https://www.youtube.com/watch?v=9TSBKO59u0Y
 - https://www.youtube.com/watch?v=MuMs1pLuT7I
 - https://www.youtube.com/watch?v=oZGmHNZv7Sc
 - https://www.youtube.com/watch?v=RczQp3zCPXs
 - https://www.youtube.com/watch?v=-lRgL9kj_h0
 - https://www.youtube.com/watch?v=QTAYRmMsVCI
 - https://www.youtube.com/watch?v=rin7gb9kdpk
 - https://www.youtube.com/watch?v=edOmvng5IQc
 - https://www.youtube.com/watch?v=nleI7IbpGhc

## Assignment review
 - client
 - server
 - HTTP request
 - request
 - response
 - socket
 - port
 - packet
 - content-type
 - status
 - npm
 - package.json
 - express
 - Routes
 - Route params
 - Views / Templates (ejs)
 - query string
 - GET, POST, PUT, DELETE
 - Run a webserver with node
 - curl

## Workshop

### Echo server with date
```javascript
var server = http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hey! How are you?');
});


server.listen(3000, '127.0.0.1');
```

#### Excercise
Create a webserver that can receive any request to any path.
It should respond the path name, the request methos and the current time.

### Rewrite it with express
```javascript
var app = express();

app.get('/', function(req, res) {
  res.send('Hey! How are you?');
});

app.listen(3000);
```

#### Excercise
Please rewrite the last example with express

### Todo app



### Add query strings
