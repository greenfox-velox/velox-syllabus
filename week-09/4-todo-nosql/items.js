"use-strict"

var mongoClient = require("./mongoClient.js").mongoClient;
var ObjectId = require('mongodb').ObjectID;
var collectionName = "todos";

var TodoItem = function () {
  this.id = nextId();
  this.text = "";
  this.completed = false;
}

TodoItem.prototype.update = function(attributes) {
  this.text = attributes.text || "";
  this.completed = !!attributes.completed;
};

var currId = 0;
function nextId() {
  return ++currId;
}

var items = {};

function getItem(id, callback) {
  mongoClient(function(err, db) {
    if(err) throw err;

    db.collection(collectionName)
      .find({_id: new ObjectId(id) })
      .limit(1)
      .next(function(err, doc) {
         if(err) throw err;
         callback(doc);
         db.close();
      });
  });
}

function addItem(attributes, callback) {
  var item = new TodoItem();
  item.update(attributes);

  mongoClient(function(err, db) {
    if(err) throw err;

    db.collection(collectionName)
      .insert(item, function(err, r) {
        if(err) throw err;
        callback(r.ops[0]);
      });
  });

  return item;
}

function removeItem(id) {
  delete items[id];
}

function allItems(callback) {
  mongoClient(function(err, db) {
    if(err) throw err;

    db.collection(collectionName)
      .find({})
      .toArray(function(err, docs) {
         if(err) throw err;
         callback(docs);
         db.close();
      });
  });
}

module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems,
};
