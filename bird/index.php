<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Birds - mezzacotta</title>
</head>
<body>
<h1>Random Birds</h1>
<p>
10 random birds, perfect for boasting to birdwatchers. Reload for more.
</p>
<ul>
<?php
putenv("PYTHONIOENCODING=UTF-8");
chdir('..');
$command = escapeshellcmd('/usr/bin/python3 generique.py bird/base 10');
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
