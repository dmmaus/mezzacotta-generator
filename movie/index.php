<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Movies - mezzacotta</title>
</head>
<body>
<h1>Random Movie Descriptions</h1>
<p>
5 random movie descriptions. Reload for more.
</p>
<ul>
<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py movie/title movie/cast movie/directed movie/rating movie/synopsis 5');
$output = shell_exec($command);
$lines = explode("\n", rtrim($output));
foreach ($lines as $line)
{
    $parts = explode("~~", $line);
    $title = trim($parts[0]);
    $cast = trim($parts[1]);
    $directed = trim($parts[2]);
    $rating = trim($parts[3]);
    $synopsis = trim($parts[4]);

    echo "<li>$title<br>$cast<br>$directed<br>$rating<br><i>$synopsis</i></li>\n<br>\n";
}
?>
</ul>

<!-- footer -->
<hr>
<p>
<i><a href="../">mezzacotta Random Generators Home</a></i>
</p>

</body>
</html>
