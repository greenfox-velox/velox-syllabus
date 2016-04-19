app.factory('meals', function($http, $location) {
  return {
    url: $location.absUrl() + 'meals/',
    list: [],
    getAll: function() {
      var _this = this;
      $http.get(_this.url).then(function (response) {
        _this.list = response.data;
      });
    },
    addItem: function(newMeal) {
      var _this = this;
      $http.post(_this.url, newMeal).success(function() {
        _this.list.push(newMeal);
      });
    },
    deleteItem: function(item) {
      var _this = this;
      var url = _this.url + item.id;
      $http.delete(url).success(function() {
        var index = _this.list.indexOf(item);
        _this.list.splice(index, 1);
      });
    }
  };
});
