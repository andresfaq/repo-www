angular.module('starter')

.controller('AppCtrl', function($scope, $state, $ionicPopup, AuthService, AUTH_EVENTS) {
  $scope.username = AuthService.username();

  $scope.$on(AUTH_EVENTS.notAuthorized, function(event) {
    var alertPopup = $ionicPopup.alert({
      title: 'Unauthorized!',
      template: 'You are not allowed to access this resource.'
    });
  });

  $scope.$on(AUTH_EVENTS.notAuthenticated, function(event) {
    AuthService.logout();
    $state.go('login');
    var alertPopup = $ionicPopup.alert({
      title: 'Session Lost!',
      template: 'Sorry, You have to login again.'
    });
  });

  $scope.setCurrentUsername = function(name) {
    $scope.username = name;
  };
})

.controller('LoginCtrl', function($scope, $http ,$state, $ionicPopup, AuthService) {

  $scope.data = {};
//  console.log('Hello')

  $scope.login = function(data){
    $http({
    method: 'POST',
    url: 'http://localhost:8000/loginMovil/',
    data: data,
    headers: {'Content-Type': 'application/json'}
    }).then(function(result) {

        if(result.data.auth === "True"){
          $scope.response = result;
          $state.go('main.dash', {}, {reload: true});

        }else{
          console.log(result.auth)
          var alertPopup = $ionicPopup.alert({
                      title: 'Login failed!',
                      template: 'Please check your credentials!'
        });}
      }, function(err) {
        $scope.response = err;

          var alertPopup = $ionicPopup.alert({
         title: 'Failed!',
         template: 'Please stop!'
        });

      });
  };

  // $scope.login = function(data) {
    
    // AuthService.login(data.username, data.password).then(function(authenticated) {
    //   $state.go('main.dash', {}, {reload: true});
    //   $scope.setCurrentUsername(data.username);
    // }, function(err) {
    //   var alertPopup = $ionicPopup.alert({
    //     title: 'Login failed!',
    //     template: 'Please check your credentials!'
    //   });
    // });


})

.controller('DashCtrl', function($scope, $http, $state, $ionicPopup, AuthService) {

  $scope.data = {};

  $scope.logout = function() {
    AuthService.logout();
    $state.go('login');
  };


  $scope.performValidRequest = function(data) {

    /*$http.jsonp('http://localhost:8000/administracion/api/v1/usuario/1/?callback=JSON_CALLBACK').then(
      //http://127.0.0.1:8000/reportes/user/1/
    //$http.get('http://localhost:8000/administracion/api/v1/usuario/1/?callback=JSON_CALLBACK').then(  
      function(result) {
        console.log(result.data.codigo_cliente)
        $scope.response = result.data.username;
      }, function(err) {
        $scope.response = 'Error!';
      });*/

    $http({
    method: 'POST',
    url: 'http://localhost:8000/estadoVehiculo/',
    data: data,
    headers: {'Content-Type': 'application/json'}
    }).then(function(result) {

        $scope.response = result.data.estado

      }, function(err) {
        $scope.response = err;

      });
  };

  $scope.performUnauthorizedRequest = function() {
    $http.get('http://localhost:8100/notauthorized').then(
      function(result) {
        // No result here..
      }, function(err) {
        $scope.response = err.data.message;
      });
  };

  $scope.performInvalidRequest = function() {
    $http.get('http://localhost:8100/notauthenticated').then(
      function(result) {
        // No result here..
      }, function(err) {
        $scope.response = err.data.message;
      });
  };
})

.controller('MapCtrl', function($scope, $ionicLoading, $compile) {
      function initialize() {
        var myLatlng = new google.maps.LatLng(43.07493,-89.381388);
        
        var mapOptions = {
          center: myLatlng,
          zoom: 16,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map"),
            mapOptions);
        
        //Marker + infowindow + angularjs compiled ng-click
        var contentString = "<div><a ng-click='clickTest()'>Click me!</a></div>";
        var compiled = $compile(contentString)($scope);

        var infowindow = new google.maps.InfoWindow({
          content: compiled[0]
        });

        var marker = new google.maps.Marker({
          position: myLatlng,
          map: map,
          title: 'Uluru (Ayers Rock)'
        });

        google.maps.event.addListener(marker, 'click', function() {
          infowindow.open(map,marker);
        });

        $scope.map = map;
      }
      google.maps.event.addDomListener(window, 'load', initialize);
      
      $scope.centerOnMe = function() {
        if(!$scope.map) {
          return;
        }

        $scope.loading = $ionicLoading.show({
          content: 'Getting current location...',
          showBackdrop: false
        });

        navigator.geolocation.getCurrentPosition(function(pos) {
          $scope.map.setCenter(new google.maps.LatLng(pos.coords.latitude, pos.coords.longitude));
          $ionicLoading.hide();
        }, function(error) {
          alert('Unable to get location: ' + error.message);
        });
      };
      
      $scope.clickTest = function() {
        alert('Example of infowindow with ng-click')
      };
      
    });
