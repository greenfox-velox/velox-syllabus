"use strict"

var mongo_url = 'mongodb://localhost:27017/todoapp';
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect(mongo_url, function(err, db) {
  if(err) throw err;

  db.collection('todos').insertMany([{
    text: 'Buy milk',
    completed: false
  }, {
    text: 'Make dinner',
    completed: false
  }]);

  db.close();
});

// {
//   alanisawesome: {
//     date_of_birth: "June 23, 1912",
//     full_name: "Alan Turing"
//   },
//   gracehop: {
//     date_of_birth: "December 9, 1906",
//     full_name: "Grace Hopper"
//   }
// }
