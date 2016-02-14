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
//*******************************************************************************************************
  /*  function agregarCodigo(codigoVenta){
        $('#id_codigoVenta').val(codigoVenta);
    }
*/
//********************************************************************************************************

    $('#btBuscar').click(
        function(e){
             e.preventDefault();
             $('#contactModal').appendTo("body").modal('show'); //i have to set it in this way because i dont understand why the modal block
                                                                // the window and i can�t edit neither modal or main page ... and i found this
                                                                // way for resolve the problem. :)  it works!

    });

    $(document).on("click",".boton-seleccionar",function(){
		var codigo=$(this).parents("tr").find("td").get(2);
        var txtcodigo=$(codigo).text(); //i get the cell's content
        $('#id_codigoVenta').val(txtcodigo);
        $('#contactModal').appendTo("body").modal('hide');


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

                        //[iteradorobjeto][0]+"campo" campo=nombreCliente, apellidoCliente,codigoVenta
                        //$('#mensajeTabla').val("");

                        var head="<th>NOMBRE </th> <th>APELLIDO </th> <th>CODIGO VENTA </th> <th>SELECCIONAR </th>";
                        var html="";
                        var color="success";
                        if(data.length<1){
                              $('#mensajeTabla').html("NO SE ENCONTRARON REGISTROS");
                        }else{
                              $('#mensajeTabla').html("");
                              for( var i=0; i<data.length;i++){

                                    html+="<tr class="+color+">" +
                                               "<td>"+data[i][0].nombreCliente+"</td>" +
                                               "<td>"+data[i][1].apellidoCliente+"</td>" +
                                               "<td>"+data[i][2].codigoVenta+"</td>"+
                                               "<td  class='boton-seleccionar'>" +
                                                    "<button type='button' class='btn btn-success'>" +
                                                        "<i class='entypo-check'></i>"+
                                                    " </button>" +
                                               "</td> </tr>";
                                    if(color=="success"){
                                        color="info";
                                    }
                                    else{
                                        color="success";
                                    }

                              }
                              html+="</tbody>";
                              $('#tablaVentasHead').html(head);
                              $('#tablaVentasBody').html(html);
                        }
                        console.log("paso");
                    },
                    error: function(message){
                        alert(message+"hola error");
                        console.log(message);
                    }
                }
            );
        }
    );

    //*****************************************************************


    $("#carrosTaller").DataTable({
      responsive:true,
      "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
            }
    });
    $("#repuestosCarro").DataTable({
      responsive:true,
      "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
       }
    });
    $(document).on("click",".btmodificarRevision",function(){
        var estado=$(this).parents("tr").find("td").get(5);
        var codigoOrden=$(this).parents("tr").find("td").get(2);
        var placa=$(this).parents("tr").find("td").get(0);

        var txtEstado=$(estado).text();
        var txtOrden=$(codigoOrden).text();
        var txtPlaca=$(placa).text();

        $('#lbNumeroOrden').text(txtOrden);//we set text in the labels
        $('#lbNumeroPlaca').text(txtPlaca);

        if(txtEstado.toLowerCase()=="Cancelado".toLowerCase()){
            $('#id_estado').val('C');
        }
        else if(txtEstado.toLowerCase()=="Terminado".toLowerCase()){
            $('#id_estado').val('T');
        }
        else {
            $('#id_estado').val('E');
        }
	    $('#revisionModal').appendTo("body").modal('show');
	});
    $(document).on("click",".checkRepuesto",function(){
        if($(this).is( ":checked" )) {
            var cantidadDisponible = $(this).parents("tr").find("td").get(2);
            var cantidadSeleccionada = $(this).parents("tr").find("td").get(4);

            var txtCD = parseInt($(cantidadDisponible).text());
            var select = $('input', cantidadSeleccionada).val(); //this way we get the input's value
            $('#lbAdvertencia').text("");

            if(select==null || select=="" || select==0){
                $(this).click();
                $('#lbAdvertencia').text(" Por favor indique la cantidad del repuesto");
            }
            else if (txtCD < select) {
                $('input', cantidadSeleccionada).val(txtCD);
            }
        }else{
            $('input', $(this).parents("tr").find("td")).val(0);
        }
    });
    $('#btAgregarRepuesto').click(function(e){
          e.preventDefault();
          var codigoOrden = $('#lbNumeroOrden').text();
          var repuestos=new Array();
          console.log("codigo orden es: "+codigoOrden);
        $("input:checkbox:checked").each(function(){
            var codigoRepuesto=$(this).parents("tr").find("td").get(0);//val());
            var cantidadS=$(this).parents("tr").find("td").get(4);//val());
            var txtCR=$(codigoRepuesto).text();
            var cantidadR=$('input', cantidadS).val();
            var arrayRepuesto={codigo:txtCR, cantidad:cantidadR};
            repuestos.push(arrayRepuesto);//we add the new spare in the array
            console.log("codigoRepuesto: "+arrayRepuesto['codigo']);
            console.log("cantidadR: "+arrayRepuesto['cantidad']);
        });

        for( i=0; i<repuestos.length;i++){
            console.log(repuestos[i]);
        }
        $.ajax(
                {
                    url:'/taller/carrosTaller/agregarRepuestosVehiculo/',
                    type:'post',
                    datatype:'json',
                    data: {'codigo_Orden': codigoOrden,
                           'repuestos_array':repuestos},

                    success:function(data){
                        console.log("buen");
                    },
                    error:function(data){
                        console.log("error ljsdlfjsldfj"+data.error);
                    }
                }
        );
    });

    //*****************************************************************





});


