'use strict';

function Meal(connection) {
  this.add = function(meal, cb) {
    connection.query('INSERT INTO meal SET ?', meal, cb);
  }

  this.getAll = function(cb) {
    connection.query('SELECT * FROM meal', cb);
  } 

  this.del = function(id,cb) {
    connection.query('DELETE FROM meal WHERE id = ?', id, cb);
  }
}

module.exports = Meal;
