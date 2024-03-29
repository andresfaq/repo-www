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
    $("#repuestosTaller").DataTable({
      responsive:true,
      "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
       }
    });

    $(document).on("click",".btVerRevision",function(){
        var estado=$(this).parents("tr").find("td").get(5);
        var codigoOrden=$(this).parents("tr").find("td").get(2);
        var codigoRevision=$(this).parents("tr").find("td").get(1);
        var placa=$(this).parents("tr").find("td").get(0);
        var fechaRev=$(this).parents("tr").find("td").get(3);
        var km=$(this).parents("tr").find("td").get(4);

        var txtRevision=$(codigoRevision).text();
        var txtEstado=$(estado).text();
        var txtOrden=$(codigoOrden).text();
        var txtPlaca=$(placa).text();
        var txtfechaRev=$(fechaRev).text();
        var txtKm=$(km).text();

        $('#lbNumeroOrdenRev').text(txtOrden);
        $('#lbNumeroPlacaOrdenRev').text(txtPlaca);
        $('#estadoOrdenRev').text(txtEstado);
        $('#fechaOrdenRev').text(txtfechaRev);
        $('#kmOrdenRev').text(txtKm);
        $.ajax(
                {
                    url:'/taller/carrosTaller/verOrdenVehiculo/',
                    type:'post',
                    datatype:'json',
                    data: {'codigo_Orden': txtOrden,
                           'codigo_Revision':txtRevision},

                    success:function(data){
                        //bodyRepuestoOR
                        //console.log("dato con parse"+data.sucursal);
                        var sucursal=data.sucursal;
                        var diagnostico=data.diagnostico;
                        var jefeTaller=data.jefeTF +" "+data.jefeTL;
                        var fechaCA=data.fechaCA;
                        var listaRepuestos=data.listaRep;
                        var body=";"
                        for(var i=0; i<listaRepuestos.length;i++){
                            body+="<tr>";
                            body+="<td>"+listaRepuestos[i].repuestoN+"</td>";
                            body+="<td>"+listaRepuestos[i].repuestoDes+"</td>";
                            body+="<td>"+listaRepuestos[i].cantidadD+"</td>";
                            body+="</tr>";
                        }
                        $('#sucursalOrdenRev').text(sucursal);
                        $('#aceiteOrdenRev').text(fechaCA);
                        $('#diagnosticoOrdenRev').text(diagnostico);
                        $('#jefeOrdenRev').text(jefeTaller);
                        $('#bodyRepuestoOR').html(body);
                        $('#verRevisionModal').appendTo("body").modal('show');
                        console.log("buen envio");
                    },
                    error:function(data){
                       // $('#lbMensaje').text("Error al registrar repuestos en la orden "+codigoOrden);
                       //   $("#lbMensaje").css("color","Tomato");
                       // $('#revisionModal').appendTo("body").modal('hide');
                        console.log("error envio"+data.error);
                    }
                }
        );
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
            //var arrayRepuesto={codigo:txtCR, cantidad:cantidadR};
            var arrayRepuesto=[txtCR, cantidadR];
            repuestos.push(arrayRepuesto);//we add the new spare in the array
           // console.log("codigoRepuesto: "+arrayRepuesto['codigo']);
              console.log("codigoRepuesto: "+arrayRepuesto[0]);
            //console.log("cantidadR: "+arrayRepuesto['cantidad']);
              console.log("cantidadR: "+arrayRepuesto[0]);
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
                           'repuestos_array[]':repuestos},

                    success:function(data){
                        $('#lbMensaje').text("Se ha registrado los repuestos a la orden "+codigoOrden);
                        $("#lbMensaje").css("color","MediumSeaGreen ");
                        $('#revisionModal').appendTo("body").modal('hide');
                        console.log("buen");
                    },
                    error:function(data){
                        $('#lbMensaje').text("Error al registrar repuestos en la orden "+codigoOrden);
                          $("#lbMensaje").css("color","Tomato");
                        $('#revisionModal').appendTo("body").modal('hide');
                        console.log("error ljsdlfjsldfj"+data.error);
                    }
                }
        );
    });

    //*****************************************************************
    $(document).on("click",".btModificarRepuesto",function() {
        var nombreR=$(this).parents("tr").find("td").get(1);
        var descripcion=$(this).parents("tr").find("td").get(2);
        var cantidad=$(this).parents("tr").find("td").get(3);
        var precio=$(this).parents("tr").find("td").get(4);
        var codigo=$(this).parents("tr").find("td").get(0);

        var txtNombreR=$(nombreR).text();
        var txtDescripcion=$(descripcion).text();
        var txtCantidad=$(cantidad).text();
        var txtPrecio=$(precio).text();
        var txtCodigo=$(codigo).text();


        $('#inpNombre').val(txtNombreR);
        $('#inpDescripcion').val(txtDescripcion);
        $('#inpCantidad').val(txtCantidad);
        $('#inpPrecio').val(txtPrecio);
        $('#lbCodigoR').text(txtCodigo);

        $('#repuestoModal').appendTo("body").modal('show');
    });

    $('#btEditarRepuesto').click(function(e){
        var nombre=$('#inpNombre').val();
        var descripcion=$('#inpDescripcion').val();
        var cantidad=$('#inpCantidad').val();
        var precio=$('#inpPrecio').val();
        var codigoR=$('#lbCodigoR').text();

         $.ajax(
                {
                    url:'/taller/repuestos/modificar/',
                    type:'post',
                    datatype:'json',
                    data: {'nombre': nombre,
                           'descripcion':descripcion,
                           'cantidad':cantidad,
                           'precio':precio,
                           'codigo':codigoR},

                    success:function(data){
                        $('#lbMensaje').text("El repuesto ha sido modificado correctamente");
                        $("#lbMensaje").css("color","MediumSeaGreen ");
                        $('#repuestoModal').appendTo("body").modal('hide');
                        console.log("buen");
                    },
                    error:function(data){
                        $('#lbMensaje').text("Error no se pudo modificar el repuesto ");
                        $("#lbMensaje").css("color","Tomato");
                        $('#repuestoModal').appendTo("body").modal('hide');
                        console.log("error ljsdlfjsldfj"+data.error);
                    }
                }
        );
    });


   //******************************************************************
});


