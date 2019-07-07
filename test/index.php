<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
</head>
<body>
<h1>Test</h1>
<p>
Testing calling python from PHP:
</p>
<ul>
<li>
<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py test/base');
$output = shell_exec($command);
$output = preg_replace('/\n/', "</li>\n<li>", $output);
echo $output;
?>
</li>
</ul>
</body>
</html>
