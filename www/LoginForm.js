/**
 * modified from St.Jacques' code
 */

var display_storage = function(storage, jqo) {
   console.log("called");

    var html = "<ul>";
    for(var i=0; i<storage.length; i++) {
        var k = storage.key(i);
        var v = storage[k];

        html += k + ", you are logged in with password " + v + ". ";
        html += " ";
    }

    html += "</ul>";
    jqo.html(html);
} ;

var display_local_storage = function() {
    display_storage(localStorage, $('#local_contents'));
} ;

var logout = function() {
    localStorage.clear();
    display_local_storage();
};

$(document).ready(function() {

    $('#login_button').click(function(event) {
        logout();

        var k = $('#username').val();
        var v = $('#password').val();
        console.log('local key:value = ' + k + ':' + v);

        localStorage[k] = v;

        display_local_storage();
    });

    $('#logout_button').click(function(event) {
       logout();
    });

    display_local_storage();
});
