//AJAX for posting
function ordenador(site_url, objects, opcao) {
    $.ajax({
        url : "/"+site_url+"/__organizador_content/",
        type : "post", // http method
        data : JSON.stringify({'objects' : objects, 'opcao': opcao}), // data sent with the post request
        contentType : "application/josn; charset=utf-8",
        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr , errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
