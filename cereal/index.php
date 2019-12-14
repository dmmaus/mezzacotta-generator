<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random breakfast cereals - mezzacotta</title>
</head>
<body>
<h1>Random Breakfast Cereals</h1>
<p>
10 random breakfast cereals, perfect for starting your day with a burst of energy. Reload for more.
</p>
<ul>
<?php
chdir('..');
$command = escapeshellcmd('/usr/bin/python3 generique.py cereal/name cereal/description cereal/servingsuggestion 10');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$lines = explode("\n", rtrim($output));
foreach ($lines as $line)
{
    $parts = explode("~~", $line);
    $name = trim($parts[0]);
    $description = trim($parts[1]);
    $serving = trim($parts[2]);
    echo "<li>$name<br><i>$description</i><br><i>$serving</i></li>\n<br>\n";
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
