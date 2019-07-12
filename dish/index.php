<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Restaurant Dishes - mezzacotta</title>
</head>
<body>
<h1>Random Restaurant Dishes</h1>
<p>
5 random restaurant dishes. Reload for more.
</p>
<ul>
<li>
<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py dish/base 5');
$output = shell_exec($command);
$output = preg_replace('/\n/', "</li>\n<li>", rtrim($output));
$output = preg_replace("/'/", "’", $output);
echo $output;
?>
</li>
</ul>
</body>
</html>
