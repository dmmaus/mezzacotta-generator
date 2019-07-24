<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Board Game Descriptions - mezzacotta</title>
</head>
<body>
<h1>Random Board Game Descriptions</h1>
<p>
5 random board game descriptions. Reload for more.
</p>
<ul>
<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py game/base 5');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$lines = explode("\n", rtrim($output));
foreach ($lines as $line)
{
    echo "<li>$line</i></li>\n";
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
