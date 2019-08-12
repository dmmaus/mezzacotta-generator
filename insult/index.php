<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Mockery Most Vicious - mezzacotta</title>
</head>
<body>
<h1>Mockery Most Vicious</h1>
<p>
10 random fantasy insults, perfect for using when your <i>D&amp;D</i> bard unleashes Vicious Mockery! Reload for more.
</p>
<ul>
<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py insult/base 10');
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
