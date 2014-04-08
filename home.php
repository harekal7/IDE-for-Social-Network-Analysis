<?php
  if ( !isset($_SESSION['is_logged_in']) || ( isset($_SESSION['is_logged_in']) && $_SESSION['is_logged_in']==0 ) )
  { 
    header("Location: index.php");
  }
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
  
    <title>SNAIDE</title>

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/bootstrap-theme.min.css" rel="stylesheet">
    <link href="css/theme.css" rel="stylesheet">  
  
  </head>

  <body role="document">

    <!-- Fixed navbar -->
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="index.php">SNAIDE</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="home.php">Home</a></li>
            <li><a href="offline.html">Access Offline</a></li>
            <li><a href="about.html">Documentation</a></li>
          </ul>
          <button type="button" class="btn btn-lg btn-danger" id="button-right" onclick="logout.php">Log Out</button>
        </div>
      </div>
    </div>  

    
    <div class="container theme-showcase" role="main">
      <div class="jumbotron">
        <form id="python-code" action="server.php" method="POST">
              <textarea id="t1" name="t2">import snaide</textarea>
        </form>
        <button id="run" type="button" class="btn btn-lg btn-success">Run</button>
        <button id="clear" type="button" class="btn btn-lg btn-danger">Clear</button>
      </div>
    </div>
    
    <div class="container theme-showcase" role="main">
      <span>Output </span>
      <pre id="out"></pre>
    </div>

    <div class="container theme-showcase" role="main">
      <label>Click on Get to download the whole database</label>
      <button id="download" type="button" class="btn btn-lg btn-default">Get</button>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/jquery.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/bootstrap-dropdown.js"></script>

    <!--Codemirror Stuffs-->
    <script src="codemirror/lib/codemirror.js"></script>
    <link rel="stylesheet" href="codemirror/lib/codemirror.css">
    <script src="codemirror/mode/python/python.js"></script>
    <link rel="stylesheet" href="codemirror/theme/cobalt.css">
    <!--<script src="js/docs.min.js"></script>-->
    
    <script type="text/javascript">
      $(document).ready(function(){
        username = window.location.href.split("=")[1];
        $("#out").html("");


        $.ajax({
           url:username+".py",
           type:"GET",
           dataType:"text",
           success:function(data)
           {
              editor.getDoc().setValue(data);
           }
        });

        var editor = CodeMirror.fromTextArea(document.getElementById("t1"), 
        {
          lineNumbers: true,
          mode: "text/x-python",
          theme: "cobalt",
          indentWithTabs: true,
          readOnly: false
        } );

        $("#run").click(function(){
          editor.save();
        	alert(editor.getDoc().getValue());
          $.ajax({
            url:"server.php",
            type:"POST",
            dataType:"text",
            data: { "t1" : $("#t1").val(), "username": username  },
            success:function(data)
            {
              $("#out").html(data);
            }
          });
        });

        $("#download").click(function(){
          $.ajax({
            url:"download.php",
            type:"POST",
            dataType:"text",
            data: { "t1" : $("#t1").val(), "username": username  },
            success:function(data)
            {
              window.location.href = "http://localhost/IDE/gdb.txt";
            }
          });
        });
        
        $("#clear").click(function(){
           $("#out").html("");
	});
      });
    </script>
  </body>
</html>
