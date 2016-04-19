app.factory('meals', function($http, $location) {
	var base_url = $location.absUrl() + 'meals/';
	var meals = [];

  function getAll() {
    return meals;
  }

  function fetchAll() {
    $http.get(base_url).then(function (response) {
      meals = response.data;
    });
  }

  return {
    getAll: getAll,
    fetchAll: fetchAll,
    addItem: function(newMeal) {
      $http.post(base_url, newMeal).success(function() {
        meals.push(newMeal);
      });
    },
    deleteItem: function(item) {
      var url = base_url + item.id;
      $http.delete(url).success(function() {
        var index = meals.indexOf(item);
        meals.splice(index, 1);
      });
    }
  };
});
