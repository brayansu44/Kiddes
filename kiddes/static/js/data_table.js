$(document).ready(function() {
    if ($.fn.DataTable.isDataTable("#example2")) {
        $("#example2").DataTable().destroy();
    }

    var table = $('#example2').DataTable({
        lengthChange: false,
        dom: 'Bfrtip',  // Necesario para mostrar los botones
        buttons: ['copy', 'excel', 'pdf', 'print'],
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json"
        },
        initComplete: function() {
            console.log("Traducción cargada correctamente.");
        }
    });

    table.buttons().container()
        .appendTo('#example2_wrapper .col-md-6:eq(0)');
});
