var app = angular.module('clienteApp', []);

app.controller('clientesCtrl', function($scope, $http) {

    $scope.cargarPlacas = function() {
        url = "http://localhost:8000/administracion/api/v1/datosventas/?usuario="+ document.getElementById('idUsuario').value+"&callback=JSON_CALLBACK"
        $http.jsonp(url

        ).then( function(response){

                $scope.datos = response.data.objects;


        }, function(response){

                alert("Error al cargar vehiculos");

        });



    };


    $scope.cargarRevisiones = function(codVenta) {
        url = "http://localhost:8000/administracion/api/v1/datosrevision/?cod_ven="+codVenta+"&callback=JSON_CALLBACK"
        $http.jsonp(url

        ).then( function(response){

                $scope.revisiones = response.data.objects;


        }, function(response){

                alert("Error al cargar revisiones");

        });



    };

    $scope.cargarOrden = function(urlOrden) {
        url = "http://localhost:8000"+urlOrden+"?callback=JSON_CALLBACK"
        $http.jsonp(url

        ).then( function(response){


                $scope.orden = response.data;
                if($scope.orden.estado == "T"){
                    $scope.estado = 'Terminado'
                }else{
                    $scope.estado = 'NA'
                }
                if($scope.orden.estado == "C"){
                    $scope.estado = 'Completado'
                }
                if($scope.orden.estado == "E"){
                    $scope.estado = 'En Espera'
                }


        }, function(response){

                alert("Error al cargar orden");

        });



    };



});
