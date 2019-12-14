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
putenv("PYTHONIOENCODING=UTF-8");
chdir('..');
$command = escapeshellcmd('/usr/bin/python3 generique.py game/title game/desc-paragraph-1 game/desc-paragraph-2 game/desc-paragraph-3 5');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$lines = explode("\n", rtrim($output));
foreach ($lines as $line)
{
    $parts = explode("~~", $line);
    $name = trim($parts[0]);
    $desc1 = trim($parts[1]);
    $desc2 = trim($parts[2]);
    $desc3 = trim($parts[3]);
    echo "<li><b>$name</b><br>$desc1<br>$desc2<br>$desc3</li>\n<br>\n";
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
