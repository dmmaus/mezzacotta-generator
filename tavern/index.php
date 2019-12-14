<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Random Tavern Names - mezzacotta</title>
<style>
body {
  background-color: #E4F8F8;
}
</style>
</head>

<body>
<img src="tavern.png" width="813" height="320" alt="[tavern image]" srcset="tavern_2x.png 2x" align="right">
<h1>Random Tavern names</h1>
<p>
10 random tavern names. Reload for more.
</p>
<ul>
<?php
putenv("PYTHONIOENCODING=UTF-8");
chdir('..');
$command = escapeshellcmd('/usr/bin/python3 generique.py tavern/base 10');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$output = preg_replace("/</", "&lt;", $output);
$output = preg_replace("/>/", "&gt;", $output);
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
<i>Tavern art: <a href="https://creativecommons.org/licenses/by/3.0/deed.en">Creative Commons Attribution 3.0 Unported</a> by <a href="https://commons.wikimedia.org/wiki/File:Bridge-medieval-fantasy-city.png">David Revoy</a>.</i>
</p>
<p>
<i><a href="../">mezzacotta Random Generators Home</a></i>
</p>

</body>
</html>
