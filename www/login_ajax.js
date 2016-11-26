function displayResult() {$"#login"}.click(function getInfo() {
	var username = $("input#username").val();
	var password = $("input#password").val();

	$.ajax({
		type: "POST",
		url: "/cgi-bin/login_check.py",
		data: authenticate(username, password);
		dataType: text}).done(function check(data){
      if(data == 2) {
        $('#result').html("Success!");
      }
      else if(data == 3){
        $('#result').html("Incorrect username or password. Please try again.");
      }
      else if(data == 1){
        $('#result').html("That username does not exist. Please create an account.");
      }
  }});

    /*
		success: function(data){
		if(data == 2) {
			$('.result').html("Success!");
		}
		else if(data == 3){
			$('.result').html("Incorrect username or password. Please try again.");
		}
		else if(data == 1){
			$('.result').html("That username does not exist. Please create an account.");
		}
	}
			return false;*/
	//	});
	//});
