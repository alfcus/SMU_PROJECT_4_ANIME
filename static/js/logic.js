$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        makePredictions();
    });

    $("#filter2").click(function() {
        makePredictions();
    });
});

// call Flask API endpoint
function makePredictions() {
    var genre = $("#genre").val();
    var score = $("#score").val();
    var animeName = $("#animeName").val();

    // create the payload
    var payload = {
        "genre": genre,
        "score": score,
        "animeName": animeName
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);

            var anime = JSON.parse(returnedData)

            console.log(anime)

            $.each(anime , function(index, item) { 
                console.log("Name: " + item["Name"]);
                console.log("English name: " + item["English name"]);
            });

            let table = '<thead><tr><th style="background-color:#FAD52D">Name</th><th style="background-color:#FAD52D">English Name</th><th style="background-color:#FAD52D">Score</th><th style="background-color:#FAD52D">Genres</th></tr></thead><tbody>';

            $.each(anime , function(index, item) { 
                table += '<tr><td style="background-color:#FAD52D">'+item["Name"]+'</td>';
                table += '<td style="background-color:#FAD52D">'+item["English name"]+'</td>';
                table += '<td style="background-color:#FAD52D">'+item["Score"]+'</td>';
                table += '<td style="background-color:#FAD52D">'+item["Genres"]+'</td></tr>';
            });

            table += '</tbody>';

            $('#output').empty().html(table);
            
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}