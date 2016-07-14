# Todo application backend with Mongodb

## Materials

- https://www.youtube.com/watch?v=qUV2j3XBRHc
- https://www.youtube.com/watch?v=CvIr-2lMLsk
- https://www.youtube.com/watch?v=-0X8mr6Q8Ew
- http://blog.modulus.io/mongodb-tutorial

Optional:

* [NoSQL on Wikipedia][1]
* [NoSQL Databases Explained][2]

Fun:

* [NoSQL comic on geek and poke][3]

## Assignment review
- noSql
- mongodb
- database
- collection
- document
- datatypes
    - string
    - integer
    - boolean
    - double
    - arrays
    - timestamp
    - object
    - null
    - symbol
    - date
- insert
- update
- delete
- query
    - pretty
    - find
    - query selectors
    - aggregators
    - limit
    - skip
    - count

## Workshop

### Set up mongodb
- In the materials there were references how to install Mongodb on your system, so install it :)
    - Ubuntu users can apt-get `mongodb-org`: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
- Start the Mongo daemon (`mongod`)
- Test if mongo is runnable, type `mongo` in your terminal
- If so, exit and import the [test data](restaurants.json):
```
$ mongoimport --db test --collection restaurants --drop --file ~/Downloads/restaurants.json
```
- This will import the test data to the test database's restaurants collection

### Tasks

[MongoDB Cheat Sheet 1](https://www.cheatography.com/ovi-mihai/cheat-sheets/mongodb/)
[MongoDB Cheat Sheet 2](https://blog.codecentric.de/files/2012/12/MongoDB-CheatSheet-v1_0.pdf)

- start a mongo client by typing `mongo` and

#### Write a mongodb query

- to display all the documents in the collection restaurants.
```
db.restaurants.find()
```
- to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.
- to display the fields restaurant_id, name, borough and cuisine, but exclude the field `_id` for all the documents in the collection restaurant.
- to display the fields restaurant_id, name, borough and zipcode, but exclude the field `_id` for all the documents in the collection restaurant.
- to display all the restaurant which is in the borough Bronx.
- to display the first 5 restaurant which is in the borough Bronx.
- to display the next 5 restaurants after skipping first 5 which are in the borough Bronx.
- to find the restaurants who achieved a score more than 90.
- to find the restaurants that achieved a score, more than 80 but less than 100.
- to find the restaurants which locates in latitude value less than -95.754168.
- to find the restaurants that does not prepare any cuisine of 'American' and their grade score more than 70 and lattitude less than -65.754168.
- to find the restaurants which does not prepare any cuisine of 'American' and achieved a score more than 70 and not located in the longitude less than -65.754168.
- Note: Do this query without using $and operator.
- to find the restaurants which does not prepare any cuisine of 'American ' and achieved a grade point 'A' not belongs to the borough Brooklyn. The document must be displayed according to the cuisine in descending order.
- to find the restaurant Id, name, borough and cuisine for those restaurants which contains 'Wil' as first three letters for its name.
- to find the restaurant Id, name, borough and cuisine for those restaurants which contains 'ces' as last three letters for its name.
- to find the restaurant Id, name, borough and cuisine for those restaurants which contains 'Reg' as three letters somewhere in its name.
- to find the restaurants which belongs to the borough Bronx and prepared either American or Chinese dish.
- to find the restaurant Id, name, borough and cuisine for those restaurants which belongs to the borough Staten Island or Queens or Bronxor Brooklyn.
- to find the restaurant Id, name, borough and cuisine for those restaurants which are not belonging to the borough Staten Island or Queens or Bronxor Brooklyn.
- to find the restaurant Id, name, borough and cuisine for those restaurants which achieved a score which is not more than 10.
- to find the restaurant Id, name, borough and cuisine for those restaurants which prepared dish except 'American' and 'Chinees' or restaurant's name begins with letter 'Wil'.
- to find the restaurant Id, name and grades for those restaurants which achieved a grade of "A" and scored 11 on an ISODate "2014-08-11T00:00:00Z" among many of survey dates..
- to find the restaurant Id, name and grades for those restaurants where 2nd element of grades array contains a grade of "A" and score 9 on an ISODate "2014-08-11T00:00:00Z".
- to find the restaurant Id, name, address and geographical location for those restaurants where 2nd element of coord array contains a value which is more than 42 and upto 52..
- to arrange the name of the restaurants in ascending order along with all the columns.
- to arrange the name of the restaurants in descending along with all the columns.
- to arranged the name of the cuisine in ascending order and for those same cuisine borough should be in descending order.
- to know whether all the addresses contains the street or not.
- which will select all documents in the restaurants collection where the coord field value is Double.
- which will select the restaurant Id, name and grades for those restaurants which returns 0 as a remainder after dividing the score by 7.
- to find the restaurant name, borough, longitude and attitude and cuisine for those restaurants which contains 'mon' as three letters somewhere in its name.
- to find the restaurant name, borough, longitude and latitude and cuisine for those restaurants which contains 'Mad' as first three letters of its name.
([here are the solutions](http://www.w3resource.com/mongodb-exercises/))

### Change the database behind your Todo API to Mongo
- Install mongodb node package:
```
npm install mongodb
```
- Setup connection, and modify the endpoints
```javascript
var mongodb = require('mongodb');
var MongoClient = mongodb.MongoClient;

// Connection URL. This is where your mongodb server is running.
var url = 'mongodb://localhost:27017/my_database_name';

// Use connect method to connect to the Server
MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    //HURRAY!! We are connected. :)
    console.log('Connection established to', url);

    // do some work here with the database.

    //Close connection
    db.close();
  }
});
```


[1]: https://en.wikipedia.org/wiki/NoSQL
[2]: https://www.mongodb.com/nosql-explained
[3]: http://geekandpoke.typepad.com/geekandpoke/2011/01/nosql.html
