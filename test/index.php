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

function my_shell_exec($cmd, &$stdout=null, &$stderr=null) {
    $proc = proc_open($cmd,[
        1 => ['pipe','w'],
        2 => ['pipe','w'],
    ],$pipes);
    $stdout = stream_get_contents($pipes[1]);
    fclose($pipes[1]);
    $stderr = stream_get_contents($pipes[2]);
    fclose($pipes[2]);
    return proc_close($proc);
}

putenv("PYTHONIOENCODING=UTF-8");
chdir('..');
$command = escapeshellcmd('/usr/bin/python3 generique.py test/base 10');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$lines = explode("\n", rtrim($output));
foreach ($lines as $line)
{
    echo "<li>$line</i></li>\n";
}
echo "</ul>\n";

echo "<p>stdout:</p>\n<p>$stdout</p>\n";
echo "<p>stderr:</p>\n<p>$stderr</p>\n";

?>

<!-- footer -->
<hr>
<p>
<i><a href="../">mezzacotta Random Generators Home</a></i>
</p>

</body>
</html>
