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

#### Routes

All routes expects and returns JSON documents.

##### `GET /todos`

List all todo items.

    $ curl localhost:3000/todos/ -s | python -m json.tool
    [
        {
            "completed": false,
            "id": 1,
            "text": "Buy milk"
        },
        {
            "completed": false,
            "id": 2,
            "text": "Make dinner"
        },
        {
            "completed": false,
            "id": 3,
            "text": "Save the world"
        }
    ]

##### `GET /todod/:id`

Get a single todo item.

    $ curl localhost:3000/todos/1 -s | python -m json.tool
    {
        "completed": false,
        "id": 1,
        "text": "Buy milk"
    }

##### `POST /todos`

Create a new todo item. Use the body of the POST request. The request must have
the `Content-Type` header set to `application/json`.

The body of the request should be a JSON document:

    {
        "text": "Description of the item",
        "completed": false
    }

The `completed` field is optional and it will default to `false`.

Example:

    $ curl localhost:3000/todos -d '{"text": "Buy eggs"}' -H'Content-Type: application/json' -s | python3 -m json.tool
    {
        "id": 4,
        "text": "Buy eggs",
        "completed": false
    }

##### `PUT /todos/:id`

Update a todo item.

Similarly to the `POST /todos` request `Content-Type` must be set to `application/json` and the body of the request must be a JSON document.

    {
        "text": "Description of the item",
        "completed": false
    }

Every field is required.

Example:

    $ curl localhost:3000/todos/4 -d '{"text": "Buy eggs and sugar", "completed": true}' -H'Content-Type: application/json' -s -XPUT | python3 -m json.tool
    {
        "id": 4,
        "text": "Buy eggs and sugar",
        "completed": true
    }

##### `DELETE /todos/:id`

Delete a todo item.

    $ curl localhost:3000/todos/4 -XDELETE -s | python3 -m json.tool
    {
        "id": 4,
        "text": "Buy eggs and sugar",
        "completed": true,
        "destroyed": true
    }

##### Errors

If a todo item is not found `404` is returned

    $ curl localhost:3000/todos/42 -i
    HTTP/1.1 404 Not Found
    X-Powered-By: Express
    Content-Type: application/json; charset=utf-8
    Content-Length: 26
    ETag: W/"1a-k6qNFtmn7O8atwPHaaY6DA"
    Date: Sat, 09 Jan 2016 18:29:55 GMT
    Connection: keep-alive

##### Frontend

Connect the application with your frontend, by serving the applications html
on: `localhost:3000/index.html`
 
##### Filter `GET /todos`

List only the completed todo items.

    $ curl localhost:3000/todos/?completed=true -s | python -m json.tool
    [
        {
            "completed": true,
            "id": 2,
            "text": "Make dinner"
        },
        {
            "completed": true,
            "id": 3,
            "text": "Save the world"
        }
    ]
