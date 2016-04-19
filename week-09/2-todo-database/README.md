# Todo application backend

## Run the server

    $ cd /path/to/backend
    $ npm install
    $ node server.js

Visit http://localhost:3000 in your browser.

## Routes

All routes expects and returns JSON documents.

### `GET /todos`

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

### `GET /todod/:id`

Get a single todo item.

    $ curl localhost:3000/todos/1 -s | python -m json.tool
    {
        "completed": false,
        "id": 1,
        "text": "Buy milk"
    }

### `POST /todos`

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

### `PUT /todos/:id`

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

### `DELETE /todos/:id`

Delete a todo item.

    $ curl localhost:3000/todos/4 -XDELETE -s | python3 -m json.tool
    {
        "id": 4,
        "text": "Buy eggs and sugar",
        "completed": true,
        "destroyed": true
    }

### Errors

If a todo item is not found `404` is returned

    $ curl localhost:3000/todos/42 -i
    HTTP/1.1 404 Not Found
    X-Powered-By: Express
    Content-Type: application/json; charset=utf-8
    Content-Length: 26
    ETag: W/"1a-k6qNFtmn7O8atwPHaaY6DA"
    Date: Sat, 09 Jan 2016 18:29:55 GMT
    Connection: keep-alive

    {"error":"Item not found"}
