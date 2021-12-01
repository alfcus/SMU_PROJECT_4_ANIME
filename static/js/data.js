$(document).ready(function() {

    buildTable(); 

}); 

function buildTable() {
    d3.csv("static/data/anime.csv").then(function(animeData) {

        var filteredData = animeData
            
        buildTableString(filteredData);
    }); 
}

function buildTableString(animeData) {

    // JQUERY creates an HTML string
    var tbody = $("#table>tbody");
    //clear table
    tbody.empty();

    //destroy datatable
    $("table").DataTable().clear().destroy();

    var datarows = animeData.map(x => [x["Name"], x["Score"], x["Genres"], x["English name"],  x["Type"], x["Episodes"], x["Aired"], x["Status"], x["Premiered"], x["Producers"], x["Licensors"], x["Studios"], x["Source"] ,x["Rating"],x["Ranked"],x ["Popularity"]])

    //redraw
    $("#table").DataTable({

        data: datarows,
        "defaultContent": "", 

        "pageLength": 10, 
        dom: 'Bfrtip', //lbfrtip if you want the length changing thing
        buttons: [
            { extend: 'copyHtml5' },
            { extend: 'excelHtml5' },
            { extend: 'csvHtml5' },
            {
                extend: 'pdfHtml5',
                title: function() { return "Dallas Crime Data"; },
                orientation: 'portrait',
                pageSize: 'LETTER',
                text: 'PDF',
                titleAttr: 'PDF'
            }
        ]
    });
}; 