"use strict"

var express = require("express");
var bodyParser = require("body-parser");
var items = require("./items.js");
var users = require("./users.js");

var app = express();

users.add({
    name: 'test',
    country: 'Hungary',
    birthdate: '1990.01.01'
});

users.get();

items.add({text: 'Buy milk'});
items.add({text: 'Make dinner'});
items.add({text: 'Save the world'});

// Basic middlewares
app.use(logRequest);
app.use(express.static("public"));
app.use(bodyParser.json());

// GET /todos => list all todo items
app.get("/todos", function (req, res) {
  res.json(items.all());
});

// POST /todos => create a new todo item
// Request body must be a valid json:
//
//    {
//      "text": "Description of the item",
//      "completed": false
//    }
//
// The +completed+ field is optional and will default to +false+.
// In the response the new todo item is returned.
app.post("/todos", function (req, res) {
  var item = items.add(req.body);
  res.status(201).json(item);
});

// GET /todos/1 => gets a single todo item
app.get("/todos/:id", function (req, res) {
  findItem(req, res, function (item) { res.json(item); });
});

// PUT /todos/1 => edit a todo item
// It accepts the same body as the POST /todos request.
app.put("/todos/:id", function (req, res) {
  findItem(req, res, function (item) {
    item.update(req.body);
    res.json(item);
  });
});

// DELETE /todos/1 => remove a todo item
// It deletes and returns a todo item.
app.delete("/todos/:id", function (req, res) {
  findItem(req, res, function (item) {
    items.remove(item.id);
    item.destroyed = true;
    res.json(item);
  });
});

app.listen(3000, function () {
  console.log("Listening on port 3000...")
});

function findItem(req, res, found) {
  var id = parseInt(req.params.id);
  var item = items.get(id);
  if (item) {
    found(item);
  } else {
    res.status(404).json({error: "Item not found"})
  }
}

function logRequest(req, res, next) {
  var parts = [
    new Date(),
    req.method,
    req.originalUrl,
  ];
  console.log(parts.join(" "));

  next();
}
