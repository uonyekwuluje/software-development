<?php
  /* Database credentials. Assuming you are running MySQL
  server with default setting (user 'root' with no password) */
  define('DB_SERVER', 'localhost');
  define('DB_USERNAME', 'empadmin');
  define('DB_PASSWORD', 'p^7ass#wor1dB34#945');
  define('DB_NAME', 'employee_db');
 
  /* Attempt to connect to MySQL database */
  $link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
 
  // Check connection
  if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
  }
?>
