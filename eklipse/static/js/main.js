let lastSearch = null;

$(document).keydown(function (e) {

    if ($(".form-control:focus") && (e.keyCode === 13)) {
        var input = $('.form-control').val();

        if (lastSearch === input) {
            $('.form-control').val('');
            return;
        } else {
            $('.form-control').val('');
            $("tbody").children().remove();
            $("#errors").children().remove()

            ajaxFunc(input)
            lastSearch = input
        }
    }
});

function button() {
    var input = $('.form-control').val();

    if (lastSearch === input) {
        $('.form-control').val('');
        return;
    } else {
        $('.form-control').val('');;
        $("tbody").children().remove();
        $("#errors").children().remove()
        
        ajaxFunc(input)
        lastSearch = input
    }
}


function ajaxFunc(input) {
    search = input
    var eklipseAPI = "/query/" + input;
    $.getJSON(eklipseAPI, {
        format: "json"
    })
        .done(function (response) {
            if (response.data == "No data found"){
                $("#errors").children().remove()
                $('<p>').text('Could not find any data about the given area.').appendTo("#errors")
            }else{
            $.each(response.data, function (i, item) {
                $('<tr>').append(
                    $('<td>').text(item.geoArea),
                    $('<td>').text(item.date),
                    $('<td>').text(item.time),
                    $('<td>').text(item.solarEclipseType),
                    $('<td>').text(item.centralDuration),
                    $('<td>').text(item.magnitude),
                    $('<td>').text(item.location),
                    $('<td>').text(item.saros),
                    $('<td>').text(item.pathWidthKM),
                    $('<td>').text(item.pathWidthMI),
                ).appendTo('#table');
            });
            }
        });
}
