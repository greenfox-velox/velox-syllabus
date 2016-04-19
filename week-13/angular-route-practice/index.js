var app = angular.module('route-test', ['ui.router']);

app.controller('Main', function($scope) {
  $scope.name = 'Tibborka';
});

app.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise('/');

  $stateProvider
    .state('main', {
      url: '/',
      templateUrl: 'main.html'
    })
    .state('vip', {
      url: '/vip',
      templateUrl: 'vip.html'
    })
});
