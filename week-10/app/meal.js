'use strict';

var mysql = require('mysql');

var connection = mysql.createConnection({
  host : 'localhost',
  user : 'root',
  password : process.env.MYSQL_PASS || '',
  database : 'calorie'
});

connection.connect();


function add(meal, cb) {
  connection.query('INSERT INTO meal SET ?', meal, cb);
}

function getAll(cb) {
  connection.query('SELECT * FROM meal', cb);
} 

function del(id,cb) {
  connection.query('DELETE FROM meal WHERE id = ?', id, cb);
}

module.exports = {
  add: add,
  getAll: getAll,
  del: del
};
