/**
 * Created by Cristian Fabian on 25/01/2016.
 */

$(document).ready(function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
//********************************************************************************************************

    $('#btBuscar').click(
        function(e){
             e.preventDefault();
             $('#contactModal').appendTo("body").modal('show'); //i have to set it in this way because i don understand why the modal block
                                                                // the window and i can´t edit neither modal or main page ... and i found this
                                                                // way for resolve the problem. :)  it works!

    });

    $('#btBuscarVentaCliente').click(
        function(e){
            e.preventDefault();
            var consulta = $('#id_buscarVenta').val();//in django for the get the value of input or whatever element of django form
                                                      // the id is equal = id_item where item is the name of element and id is only prefix "id"
            $.ajax(
                {
                    url:'/taller/busquedaCodigoVenta/',
                    type:'post',
                    datatype:'json',
                    data: {'nombreCliente': consulta},

                    success:function(data){
                        console.log(data)
                    },
                    error: function(message){
                        alert(message+"hola error")
                        console.log(message);
                    }
                }
            )
        }
    );



});


