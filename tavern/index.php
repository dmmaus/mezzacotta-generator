<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
</head>
<body>
<h1>Random Tavern names</h1>
<p>
10 random tavern names. Reload for more.
</p>
<ul>
<li>
<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py tavern/base');
$output = shell_exec($command);
$output = preg_replace('/\n/', "</li>\n<li>", $output);
echo $output;
?>
</li>
</ul>
</body>
</html>
