<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Laws from around the world - mezzacotta</title>
</head>
<body>
<h1>Random Laws</h1>
<p>
10 random weird laws from around the world. Reload for more.
</p>
<ul>
<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py law/base 10');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$lines = explode("\n", rtrim($output));
foreach ($lines as $line)
{
    $parts = explode("~~", $line);
    $law = trim($parts[0]);
    echo "<li>$law</li>\n<br>\n";
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
