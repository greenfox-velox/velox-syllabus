# Wednesday - Node.js and MySQL

## Materials
- https://www.youtube.com/watch?v=XuLRKMqozwA
- https://www.sitepoint.com/using-node-mysql-javascript-client/

## Docs for today
https://github.com/mysqljs/mysql

## Assignment review
- relational database
- SQL
- primary key
- create database
- use database
- create table
- text varchar integer datetime
- insert into
- value / values
- select
    - where
    - operators (= > < <> IN)
    - group by
    - having
    - sql functions (sum max min avg)
- createConnection
- connect
- end
- query

## Workshop

### Connect to database
```JavaScript
var mysql = require("mysql");

var con = mysql.createConnection({
  host: "localhost",
  user: "'jaj'",
  password: "alma"
});

con.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

con.end();
```


### Querying a database
```JavaScript
con.query("SELECT * FROM table_name;",function(err,rows){
  console.log("Data received from Db:\n");
  console.log(rows);
});
```

### Error handling
```JavaScript
con.query("SELECT * FROM table_name;",function(err,rows){
  if(err) {
    console.log(err.toString());
    return;
  }

  console.log("Data received from Db:\n");
  console.log(rows);
});
```

#### Exercises
- use yesterday's database through node. create a query and write to the console:
 1. all book names
 2. all books with its name, authors name, category name, publishers name and price

### MySQL and Express
 ```JavaScript
 var app = express();

 app.get('/', function(req, res) {
   con.query('SELECT book_name FROM book_mast;',function(err,rows){
     if(err) {
       console.log(err.toString());
       return;
     }
     res.send(rows);
   });
 });
 ```

#### Exercises
- use yesterday's database through node and express. create an endpoint that returns:
  1. all book names
  2. all books with its name, authors name, category name, publishers name and price


### Todo app

  Extend Monday's todo app endpoints with mysql queries.

#### Routes

  All routes expects and returns JSON documents.

##### `GET /todos`

  List all todo items.

##### `GET /todod/:id`

  Get a single todo item.

##### `POST /todos`

  Create a new todo item. Use the body of the POST request. The request must have
  the `Content-Type` header set to `application/json`.

##### `PUT /todos/:id`

  Update a todo item.

  Similarly to the `POST /todos` request `Content-Type` must be set to `application/json` and the body of the request must be a JSON document.

##### `DELETE /todos/:id`

  Delete a todo item.

##### Filter `GET /todos`

  List only the completed todo items.
