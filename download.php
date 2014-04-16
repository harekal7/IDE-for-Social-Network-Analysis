<?php
	
	/*
	
	The shell command dumps the whole graph database in terms of cypher statements
	which can be used by the client to sync up their local neo4j graph database.
	The cypher statements are redirect to a gdb.txt file which can be downloaded.

	*/

	shell_exec("neo4j-shell -c dump > gdb.txt");
?>