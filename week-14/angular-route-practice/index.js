var app = angular.module('route-test', ['ui.router']);

app.controller('Main', function($scope, $rootScope, $state) {
  $scope.name = 'Tibborka';
  $scope.login = function() {
    $rootScope.user = {
      name: 'Robika'
    };
    $state.go('main-logged-in');
  };
});

app.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise('/');

  $stateProvider
    .state('main', {
      url: '/',
      templateUrl: 'main.html',
      controller: function($rootScope, $state) {
        if ($rootScope.user) {
          $state.go('main-logged-in')
        }
      } 
    })
    .state('main-logged-in', {
      url: '/',
      templateUrl: 'user.html',
      controller: function($rootScope, $state) {
        if (!$rootScope.user) {
          $state.go('main');
        }
      }
    })
    .state('vip', {
      url: '/vip',
      templateUrl: 'vip.html'
    })
});
