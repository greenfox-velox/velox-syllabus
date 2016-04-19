app.get('/todos', function (req, res) {
  items.all(function(result){
    res.json(result);
  });
});



In items.js:

function getAllTodos(cb) {
  connection.query('SELECT * FROM todo', function(err, result) {
    if (err) throw err;
    cb(result);
  });
}

module.exports = {
  all: getAllTodos,
};
