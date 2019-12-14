<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>mezzacotta Cinématique - v. 2.0</title>
<style type="text/css">
.main
{
    width: 800px;
    padding-top: 0px;
    margin-left: auto;
    margin-right: auto;
    text-align: left;
    font-family: Arial;
}

.marquee
{
    margin-top: 5px;
    margin-bottom: 5px;
    text-align: center;
}

.title
{
	width:600px;
    margin-top: 15px;
    margin-bottom: 15px;
    font-size: 20pt;
    font-style: bold;
    color:white
}

.cast
{
	width:600px;
    margin-top: 15px;
    margin-bottom: 5px;
    font-size: 11pt;
    font-style: bold;
    color:#FAFAD2
}

.rating
{
    margin-top: 15px;
    margin-bottom: 15px;
    font-size: 8pt;
    color:indianred
}

.synopsis
{
	width:600px;
    margin-top: 15px;
    margin-bottom: 15px;
    font-size: 12pt;
    font-style: italic;
    color:white
}

.epilogue
{
    margin-top: 40px;
    color:white
    font-size: 11pt;
}

.leftside
{
    float:left
    width:100px;
    margin-right:10px;
    background-color:#FF00FF
}

.break
{
    font-size: 20pt;
    font-style: normal;
}
</style>
<link rel="shortcut icon" href="/wp/wp-content/themes/mezzacotta/favicon.ico" />
<link rel="stylesheet" href="/wp/wp-content/themes/mezzacotta/style.css" type="text/css" media="screen" />

<style type="text/css" media="screen">
	#page { background: #000000; border: none; }
</style>
</head>

<body>
<div id="page">

<div class="leftside">
</div>

<br class="clear" />

<div class="marquee">
<a href="/generate/movie/"><img src="./Graphics/marquee_cinematique.png" srcset="./Graphics/marquee_cinematique_2x.png 2x" width="460" height="280" border="0" alt="Mezzacotta Cinematique"></a>
</div>

<div class="main">

<?php
putenv("PYTHONIOENCODING=UTF-8");
chdir('..');
$command = escapeshellcmd('/usr/bin/python3 generique.py movie/title movie/cast movie/directed movie/rating movie/synopsis 5');
$output = shell_exec($command);
$lines = explode("\n", rtrim($output));
$i = 0;
foreach ($lines as $line)
{
    if ($i != 0)
    {
        ?>
        <div class="marquee"><img src="./Graphics/separator.png" srcset="./Graphics/separator_2x.png 2x" width="584" height="28"></div>
        <?php
    }
    $parts = explode("~~", $line);
    $title = trim($parts[0]);
    $cast = trim($parts[1]);
    $directed = trim($parts[2]);
    $rating = trim($parts[3]);
    $synopsis = trim($parts[4]);

    echo "<div class=\"title\">$title</div>\n";
    echo "<div class=\"cast\">$cast<br>$directed</div>\n";
    echo "<div class=\"rating\">$rating</div>\n";
    echo "<div class=\"synopsis\">$synopsis</div>\n";
    
    $i++;
}
?>

<div class="marquee">
<a href="/generate/movie/"><img src="./Graphics/coming_soon.png" srcset="./Graphics/coming_soon_2x.png 2x" width="388" height="86" border="0" alt="Coming Soon"></a>
</div>

<div class="epilogue">
Brought to you by <a href="/">mezzacotta</a><br>
<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://licensebuttons.net/l/by-nc-sa/3.0/80x15.png" width="80" height="15" /></a><br />This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported Licence</a> by The Comic Irregulars. <i>d&#109;m&#64;d&#97;nger&#109;o&#117;se&#46;n&#101;t</i><br />
</div>

</div> <!-- id=main -->
<br class="clear">
</div> <!-- id=page -->

<!-- footer -->
<hr>
<p>
<i><a href="../">mezzacotta Random Generators Home</a></i>
</p>

</body>
</html>
