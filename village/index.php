<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Villages - mezzacotta</title>
</head>
<body>
<h1>Random Villages</h1>
<p>
10 random villages. Reload for more.
</p>
<ul>
<?php
putenv("PYTHONIOENCODING=UTF-8");
chdir('..');
$command = escapeshellcmd('/usr/bin/python3 generique.py village/base village/festival-base 10');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$output = preg_replace("/</", "&lt;", $output);
$output = preg_replace("/>/", "&gt;", $output);
$lines = explode("\n", rtrim($output));
foreach ($lines as $line)
{
    $parts = explode("~~", $line);
    $name = trim($parts[0]);
    $festival = trim($parts[1]);
    echo "<li>$name<br><i>$festival</i></li>\n<br>\n";
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
