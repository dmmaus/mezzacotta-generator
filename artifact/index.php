<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Artifacts - mezzacotta</title>
</head>
<body>
<h1>Random Artifacts</h1>
<p>
10 random artifacts, perfect for your party of adventurers to be searching for. Reload for more.
</p>
<ul>
<li>
<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py artifact/base 10');
$output = shell_exec($command);
$output = preg_replace('/\n/', "</li>\n<li>", rtrim($output));
$output = preg_replace("/'/", "’", $output);
echo $output;
?>
</li>
</ul>
</body>
</html>
