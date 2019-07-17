<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Villagess - mezzacotta</title>
</head>
<body>
<h1>Random Villages</h1>
<p>
10 random villages. Reload for more.
</p>
<ul>
<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py village/base 10');
$output = shell_exec($command);
$lines = explode("\n", rtrim($output));
foreach ($lines as $line)
{
    echo "<li>$line</li>\n";
}
?>
</ul>
</body>
</html>
