var app = angular.module('clienteApp', []);

app.controller('clientesCtrl', function($scope, $http) {

    $scope.cargarPlacas = function() {
        url = "http://localhost:8000/administracion/api/v1/datosventas/?usuario="+ document.getElementById('idUsuario').value+"&callback=JSON_CALLBACK"
        $http.jsonp(url

        ).then( function(response){

                $scope.datos = response.data.objects;

        }, function(response){

                alert("Fail");

        });

    };

});
