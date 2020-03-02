$(document).ready(function () {
    var callback = function() {
       $('.newscard').remove();

       // Output the value

       $.ajax({
               'type': "GET",
               'url': "json_news",
               contentType:  'application/json;charset=UTF-8',
                  success: function(response) {
                   const data = JSON.parse(response);
                   // debug**
                   //console.log(typeof(data));
                   console.log(data);

                   // looping through items in 'response' object which is a list of objects here..
                   for(i=0;i<data.length;i++) {
                       const url = data[i]['url']
                       const source = data[i]['source']['name']
                       const title = data[i]['title']
                       const image = data[i]['urlToImage']
                       const content = data[i]['content']
                       const date = data[i]['publishedAt'].replace("T"," ")
                       const myHtml = "<div class='newscard'><a href='"+url+"' target='_blank'><p class='card_a'>"+title+"</p></a><img class='newsposter' src='"+image+"'><p id='card_p'>"+date+"</p></div>";
                       // console.log(typeof(myHtml));
                       if (data) {
                           $('#div-news').append(myHtml);
                       }
                   }
              }
       })
    };

    $('#refresh').click(callback);
});