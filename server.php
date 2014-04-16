<?php


	// Retrieve all the data recieved
	$content = $_POST['t1'];
	$username = $_POST['username'];

	// for anonymous users, use a temporary file to store/retrieve the workspace
	if ($username===NULL)
	{
		$file_name = "temp";	
	}
	// for authenticated users, use their respective files to store/retrive the workspace
	else
	{	
		$file_name = "$username";	
	}

	/*
	Access the file
	update the file in the server filesystem
	update the contents of the particular file with the code written by the user
	execute the code
	also redirect the output of standard error stream to standard output stream
	so that errors are also displayed in the output in the IDE.
	*/

	$file = "/var/www/IDE/$file_name.py";
	shell_exec("rm $file; touch $file");
	file_put_contents($file, $content);
	echo shell_exec("python /var/www/IDE/$file_name.py 2>&1");
?>

