<?php
	$username = $_GET["username"];
	//shell_exec("python /var/www/IDE/update.py");
	header("Location: home.html?username=$username");
?>
