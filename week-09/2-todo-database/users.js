var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'test',
  password : 'test',
  database : 'todo'
});

connection.connect();

function addUser(attributes) {
  connection.query('INSERT INTO user SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  });
}

function updateUser(attributes) {
  connection.query('UPDATE user SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.changedRows);
  });
}

function delUser(attributes) {
  connection.query('DELETE FROM user WHERE id=1', function(err, result) {
    if (err) throw err;
    console.log(result);
  });
}

function getUser() {
  connection.query('SELECT * FROM `user`', function(err, results) {
    if (err) throw err;
    console.log(results);
  });
}

function getUserById(attributes, cb) {
  connection.query('SELECT * FROM `user` WHERE user_id=?', [attributes.user_id], function(err, results) {
    if (err) throw err;
    console.log(results);
    cb(results);
  });
}

module.exports = {
  add: addUser,
  get: getUser,
  getUserById: getUserById
};
