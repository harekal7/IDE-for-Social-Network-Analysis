<?php

	/*

	Retrieve the username recieved
	execute update.py in the server machine which syncs the graph database with elgg primary database
	redirect back to IDE main page ( home.html ) and pass on the username along with it
	which is used to retrieve the users previous workspace.

	*/

	session_start();
	$username = $_GET["username"];
	//shell_exec("python /var/www/IDE/update.py");
	header("Location: home.html?username=$username");
?>