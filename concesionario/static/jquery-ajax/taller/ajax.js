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
             $('#contactModal').appendTo("body").modal('show'); //i have to set it in this way because i don understand why the modal block
                                                                // the window and i can´t edit neither modal or main page ... and i found this
                                                                // way for resolve the problem. :)  it works!



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