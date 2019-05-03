//When a user submits the form
	$("#submit-message").click(function(){
		var clientmsg = $("#user-message").val(); //store the message
		$.post("post.php", {text: clientmsg}); //post the message
		$("#user-message").attr("value", "");
		return false;
	});
