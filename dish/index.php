<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Restaurant Dishes - mezzacotta</title>
</head>
<body>
<h1>Random Restaurant Dishes</h1>
<p>
5 random restaurant dishes. Reload for more.
</p>
<ul>
<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py dish/base dish/wine-name dish/wine-description 5');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$lines = explode("\n", rtrim($output));
foreach ($lines as $line)
{
    $parts = explode("~~", $line);
    $dish = trim($parts[0]) . ".";
    $wine = trim($parts[1]);
    $winedescription = trim($parts[2]);
    echo "<li>$dish<br>With this dish we recommend: $wine<br><i>$winedescription.</i></li>\n<br>\n";
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
