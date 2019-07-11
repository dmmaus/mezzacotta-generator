<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Board Game Descriptions - mezzacotta</title>
</head>
<body>
<h1>Random Tavern names</h1>
<p>
5 random board game descriptions. Reload for more.
</p>
<ul>
<li>
<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py game/base 5');
$output = shell_exec($command);
$output = preg_replace('/\n/', "</li>\n<li>", rtrim($output));
$output = preg_replace("/'/", "’", $output);
echo $output;
?>
</li>
</ul>
</body>
</html>
