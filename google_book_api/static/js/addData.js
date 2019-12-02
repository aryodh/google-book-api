
function find(keyword) {
    $.ajax({
        url: "/google_api/keyword="+keyword,
        datatype: 'json',
        success: function(data){
            $('tbody').empty();
            var result;
            for(var i = 0; i < data.items.length; i++) {
                result += '<tr>'
                result += "<th scope='row' class='align-middle text-center'>" + (i+1) + "</th>" +
                "<td><img class='img-fluid' style='width:22vh' src='" + data.items[i].volumeInfo.imageLinks.smallThumbnail +"'></img>" + "</td>" +
                "<td style='padding: 15px;' class='align-middle'>" + data.items[i].volumeInfo.title +"</td>" +
                "<td style='padding: 15px;' class='align-middle'>" + data.items[i].volumeInfo.authors + "</td>" + 
                "<td style='padding: 15px;' class='align-middle'>" + data.items[i].volumeInfo.publisher +"</td>" + 
                "<td style='padding: 15px;' class='align-middle'>" + data.items[i].volumeInfo.publishedDate +"</td>" + 
                "</tr>";
            }

            $('tbody').append(result);
        }
    })
}

function search() {
    var word = $('input[name="search_field"]').val();
    alert('masuk');
    find(word);
}


