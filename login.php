<?php

	/*

	Retrieve the username recieveds
	redirect back to IDE main page ( home.html ) and pass on the username along with it
	which is used to retrieve the users previous workspace.

	*/

	session_start();
	$username = $_GET["username"];
	header("Location: home.html?username=$username");
?>