<?php


	$content = $_POST['t1'];
	$username = $_POST['username'];

	if ($username===NULL)
	{
		$file_name = "temp";	
	}
	else
	{	
		$file_name = "$username";	
	}
	$file = "/var/www/IDE/$file_name.py";
	shell_exec("touch $file");
	file_put_contents($file, $content);
	echo shell_exec("python /var/www/IDE/$file_name.py 2>&1");
?>

