var meal = function(con){

  var listMeals = null;
  var deleteMeal = null;

  function addMeal (meal, callback) {
    con.query('INSERT INTO `tablecalorie` (`name`, `calorie`, `date`)' +
    ' VALUES ('+ "'" + meal.name + "'" + ', ' + "'" + meal.calories + "'" + ', ' + "'" + meal.date + "'" + ');', function(err, result){
      if(err){
        console.log(err.toString());
        return;
      }
      callback(result);
    });
  };

  return {
    listMeals: listMeals,
    addMeal: addMeal,
    deleteMeal: deleteMeal
  };
};

module.exports = meal;
