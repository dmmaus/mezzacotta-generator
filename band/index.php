<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Band Names - mezzacotta</title>
</head>
<body>
<h1>Random Band Names</h1>
<p>
10 random band names, perfect for naming your garage band before you make it big. Reload for more.
</p>
<ul>
<?php
chdir('..');
$command = escapeshellcmd('/usr/bin/python3 generique.py band/base 10');
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
