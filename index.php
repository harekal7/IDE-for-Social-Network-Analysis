<?php

	session_start();

  if ( isset($_SESSION['is_logged_in']) &&  $_SESSION['is_logged_in'] == 1 )
  {
    header("Location: home.php?username=".$_SESSION['username']);
  }

echo "<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <meta name='description' content=''>
    <meta name='author' content=''>
  
    <title>SNAIDE</title>

    <link href='css/bootstrap.min.css' rel='stylesheet'>
    <link href='css/bootstrap-theme.min.css' rel='stylesheet'>
    <link href='css/theme.css' rel='stylesheet'>

    <script src='js/jquery.js'></script>
  </head>

  <body role='document'>

    <!-- Fixed navbar -->
    <div class='navbar navbar-inverse navbar-fixed-top' role='navigation'>
      <div class='container'>
        <div class='navbar-header'>
          <button type='button' class='navbar-toggle' data-toggle='collapse' data-target='.navbar-collapse'>
            <span class='sr-only'>Toggle navigation</span>
            <span class='icon-bar'></span>
            <span class='icon-bar'></span>
            <span class='icon-bar'></span>
          </button>
          <a class='navbar-brand' href='index.php'>SNAIDE</a>
        </div>
        <div class='navbar-collapse collapse'>
          <ul class='nav navbar-nav'>
            <li><a href='home.php'>Home</a></li>
            <li><a href='offline.html'>Access Offline</a></li>
            <li><a href='about.html'>Documentation</a></li>
          </ul>
          <button type='button' class='btn btn-lg btn-danger' id='button-right' onclick='logout.php'>Log Out</button>
        </div><!--/.nav-collapse -->
      </div>
    </div>  

    <div class='container theme-showcase' role='main'>

      <!-- Main jumbotron for a primary marketing message or call to action -->
      <div class='jumbotron'>
        <h1>SNAIDE</h1>
        <p>an Integrated Development Environment for Analysing data of Social Network built using Elgg</p>
        <p><a id='login' href=\"#\" class='btn btn-primary btn-lg' role='button'>Login &raquo;</a></p>
        <div class='panel panel-primary hidden-panel'>
          <div class='panel-heading'>
            <h3 class='panel-title'>Login</h3>
          </div>
          <div class='panel-body'>
            <div id='wrong'>Wrong Username or Password. Try Again</div>
	            <form id='elgg' method='POST' action=\"http://localhost/elgg/services/api/rest/json/?method=auth.gettoken\">
	              <input id='log-t' type='text' name='username' placeholder='Username'>
	              <p></p>
	              <input id='log-p' type='password' name='password' placeholder='Password'>
	              <p><a id='log-in' href=\"#\" class='btn btn-primary btn-lg' role='button'>Login &raquo;</a></p>
	            </form>
          	</div>
        	</div>
        	<p>OR</p>
        	<p><a id='offline' href='offline.html' class='btn btn-primary btn-lg' role='button'>Access Offline &raquo;</a></p>
       	</div>
    	</div>
    </div> 
	  
	  <script src='js/bootstrap.min.js'></script>
    <script src='js/bootstrap-dropdown.js'></script>
    <script type='text/javascript'>
    $(document).ready(function(){
      $(\"#login\").click(function(){
        $(\"#login\").css({'display':'none'});
        $('.panel').css({'display':'block'});
      });
      $(\"#log-in\").click(function(){
        $(\"#wrong\").css({'display':'none'});
        $.ajax({
            url:\"http://localhost/elgg/services/api/rest/json/?method=auth.gettoken\",
            type:'POST',
            dataType:'text',
            data: { 'username' : $(\"#log-t\").val(), 'password':$(\"#log-p\").val() },
            success:function(data)
            {
              s = JSON.parse(data);
              if ( s.status >= 0 )
              {
                window.location.replace(\"update.php?username=\"+$(\"#log-t\").val());
              }
              else
              {
                $(\"#wrong\").css({'display':'block'});
              }
            }
          });
      });
    });
    </script>
  </body>
</html>
";
?>