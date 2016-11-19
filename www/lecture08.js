/**
*Testing
*/

$(document).ready(function() {
    console.log("Lecture 08 script loaded...");

    // when the button with the id 'fetch_pizza' is clocked...
    $('#submit').click(get_status);
    $('#usernamefield').keypress(function(event) {
        var key = event.which;
        if(key == 13) { // enter key event
            //get_status();
            get_status_simple();
        }
    });
});

var status_returned = function( data ) {   // function to execute upon a successful request
    console.log("success!");
    $('#error').empty();
    $('#name').html('Name: ' + data.name);
    $('#size').html('Size: ' + data.size);
    $('#crust').html('Crust: ' + data.crust);
    $('#toppings').html('Toppings: ' + data.toppings);
    $('#phone').html('Phone Number: ' + data.phone);
    $('#credit').html('Credit Card Number: ' + data.credit);
};

var get_status = function() {
    // get the value typed into the input field with the id 'customer_name'
    var $name = $('#usernamefield').val();
    console.log("name: " + $name);

    // .ajax is the core Ajax function supported by jQuery and requires the following parameters:
    //  url: the URL of the resource to send the request to
    //  data: the data to send along with the request; encoded as a query string for GET
    //  dataType: the expected format of the data coming back in the response
    //  success: a function to execute if the request is successful
    //  error: a function to execute if the request fails for any reason
    $.ajax({
        url: '../cgi-bin/login_check.py',  // lecture 8 script to query the pizza database

        data: {                       // the data to send
            usernamefield: $name
        },

        type: "POST",                  // GET or POST

        dataType: "json",             // json format

        success: function( data ) {   // function to execute upon a successful request
            console.log("success!");
            console.log(data);
            
            $('#usernamefield').html('Name: ' + data.usernamefield);
            $('#passwordfield').html('Size: ' + data.passwordfield);
            
        },

        error: function(request) {   // function to call when the request fails
            console.log("error!");
            console.log(data);
            console.log(request);
            $('.order_data').empty();
            $('#error').html("<p>There has been an error fetching the order for " + $name +
                ", are you sure that this person has an outstanding order?</p>");
        }
    });
};

var handle_error = function(request) {
    console.log("error!");
        console.log(request);
        $('.order_data').empty();
        $('#error').html("<p>There has been an error fetching the order for " + $name +
            ", are you sure that this person has an outstanding order?</p>");
    };

var get_status_simple = function() {
    var $name = $('#usernamefield').val();
    $.getJSON(
        "../cgi-bin/login_check.py",
        { usernamefield: $name },
        status_returned).fail(handle_error);
};