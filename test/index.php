<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
</head>
<body>
<h1>Test generator</h1>
<p>
10 random silly sentences with a small custom vocabulary, for test purposes. Reload for more.
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
