var mysql = require("mysql");
var express = require("express");

var con = mysql.createConnection({
  host: "localhost",
  user: "'jaj'",
  password: "alma",
  database: "bookstore"
});

//
// con.query('SELECT * FROM book_mast;',function(err,rows){
//   if(err) {
//     console.log('Error querying db:');
//     console.log(err.toString());
//     return;
//   }
//
//   console.log('Data received from Db:\n');
//   console.log(rows);
// });

var app = express();

app.get('/', function(req, res) {
  con.query('SELECT book_name FROM book_mast;',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }

    console.log('GET Data received from Db:\n');
    console.log(rows);
    res.send(rows);
  });
});

app.listen(3000);
