<?php
	shell_exec("touch /var/www/IDE/temp.py");
	$file = "/var/www/IDE/temp.py";
	$content = $_POST['t1'];
	$content = "import snaide\n".$content;
	file_put_contents($file, $content);
	echo shell_exec("python /var/www/IDE/temp.py");
	/*
	graph_db, cur1, cur2, cur3, cur4, cur5 = snaide.init("localhost", "root", "", "elgg", "http://localhost:7474/db/data/")
users = snaide.get_all_users(graph_db)
print users
	*/
?>

