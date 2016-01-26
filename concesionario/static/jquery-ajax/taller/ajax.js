/**
 * Created by Cristian Fabian on 25/01/2016.
 */

$(document).ready(function() {
        ajaxFunction();
});


function ajaxFunction(){
    $('#btBuscar').click(
        function(e){
             e.preventDefault();
             //$('#contactModal').modal('show');
            $('#contactModal').fadeIn('slow');
            $('.popup-overlay').fadeIn('slow');
            $('.popup-overlay').height($(window).height());
            return false;
    })
}


/*
$.ajax({
                type:'post',
                url:'/busqueda/',

                success:function(){
                    $(contactModal).modal('show');
                },

                error:function(){

                }

            })
 */