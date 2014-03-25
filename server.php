<?php
	shell_exec("touch /var/www/IDE/temp.py");
	$file = "/var/www/IDE/temp.py";
	$content = $_POST['t1'];
	#$content = "import snaide\n".$content;
	file_put_contents($file, $content);
	echo shell_exec("python /var/www/IDE/temp.py 2>&1");
?>

