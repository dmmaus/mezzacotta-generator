<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Text Generators - mezzacotta</title>
</head>
<body>
<h1>Test generator</h1>
<p>
10 random silly sentences with a small custom vocabulary, for test purposes. Reload for more.
</p>
<ul>
<?php
chdir('..');
$command = escapeshellcmd('/usr/bin/python3 generique.py test/base 10');
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
