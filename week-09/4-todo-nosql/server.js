"use strict"

var express = require("express");
var bodyParser = require("body-parser");
var items = require("./items.js");

var app = express();

// Basic middlewares
app.use(logRequest);
app.use(express.static("public"));
app.use(bodyParser.json());

// GET /todos => list all todo items
app.get("/todos", function (req, res) {
  items.all(function(docs) {
    res.json(docs);
  });
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
  items.add(req.body, function(doc) {
    res.status(201).json(doc);
  });
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
  var id = req.params.id;
  var item = items.get(id, function(doc) {
    if (doc) {
      found(doc);
    } else {
      res.status(404).json({error: "Item not found"})
    }
  });
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
