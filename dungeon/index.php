<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>mezzacotta DM</title>
<style type="text/css">

@font-face {
    font-family: ddFont;
    src: url('SouvenirEF-Demi.otf');
}

.main
{
    width: 800px;
    padding-top: 10px;
    margin-left: auto;
    margin-right: auto;
    text-align: left;
    font-family: Arial;
}

.marquee
{
    margin-top: 5px;
    margin-bottom: 5px;
    text-align: right;
}

.dungeon_book
{
    margin-top: 30px;
    padding: 10px;
    width: 800px;
    box-shadow: 5px 10px 8px #888888;
    border-spacing: 30px 30px;
}

p.dungeon_code
{
	width:700px;
    margin-top: 10px;
    margin-bottom: 5px;
    margin-left: 50px;
    margin-right: 50px;
    font-size: 20pt;
    font-family: ddFont;
    color:white;
    text-align: center;
}

p.dungeon_name
{
	width:600px;
    margin-top: 10px;
    margin-bottom: 15px;
    margin-left: 100px;
    margin-right: 100px;
    font-size: 25pt;
    font-family: ddFont;
    color:yellow;
    text-align: center;
}

p.author
{
	width:500px;
    margin-top: 10px;
    margin-bottom: 10px;
    margin-left: 150px;
    margin-right: 150px;
    font-size: 14pt;
    font-family: ddFont;
    color:white;
    text-align: center;
}

p.party
{
	width:600px;
    margin-top: 20px;
    margin-bottom: 10px;
    margin-left: 100px;
    margin-right: 100px;
    font-size: 14pt;
    font-family: ddFont;
    color:white;
    text-align: center;
    word-spacing: 0.35em;
}

.epilogue
{
    margin-top: 40px;
    color:white
    font-size: 11pt;
}

.break
{
    font-size: 20pt;
    font-style: normal;
}
</style>
<link rel="shortcut icon" href="http://www.mezzacotta.net/wp/wp-content/themes/mezzacotta/favicon.ico" />
<link rel="stylesheet" href="http://www.mezzacotta.net/wp/wp-content/themes/mezzacotta/style.css" type="text/css" media="screen" />

<style type="text/css" media="screen">
	#page { background-image: url('d20_bg.png')}
</style>
</head>

<body>
<div id="page">

<div class="main">

<?php
putenv("PYTHONIOENCODING=UTF-8");
chdir('..');
$command = escapeshellcmd('/usr/bin/python3 generique.py dungeon/code 3');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$output = preg_replace("/</", "&lt;", $output);
$output = preg_replace("/>/", "&gt;", $output);
$codes = explode("\n", rtrim($output));

$command = escapeshellcmd('/usr/bin/python3 generique.py dungeon/module 3');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$output = preg_replace("/</", "&lt;", $output);
$output = preg_replace("/>/", "&gt;", $output);
$modules = explode("\n", rtrim($output));

$command = escapeshellcmd('/usr/bin/python3 generique.py dungeon/attribution 3');
$output = shell_exec($command);
$output = preg_replace("/By /", "by ", $output);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$output = preg_replace("/</", "&lt;", $output);
$output = preg_replace("/>/", "&gt;", $output);
$authors = explode("\n", rtrim($output));

$command = escapeshellcmd('/usr/bin/python3 generique.py dungeon/adventure 3');
$output = shell_exec($command);
$output = strtoupper($output);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$output = preg_replace("/</", "&lt;", $output);
$output = preg_replace("/>/", "&gt;", $output);
$adventures = explode("\n", rtrim($output));
?>

    <div class="dungeon_book" style="background-image: url('red_paper.png');">

        <p class="dungeon_code">
<?php
echo $codes[0];
?>
        </p>
        <p class="dungeon_name">
<?php
echo $modules[0];
?>
        </p>
        <p class="author">
<?php
echo $authors[0];
?>
        </p>
        <p class="party">
<?php
echo $adventures[0];
?>
        </p>
    </div>

    <div class="dungeon_book" style="background-image: url('blue_paper.png');">

        <p class="dungeon_code">
<?php
echo $codes[1];
?>
        </p>
        <p class="dungeon_name">
<?php
echo $modules[1];
?>
        </p>
        <p class="author">
<?php
echo $authors[1];
?>
        </p>
        <p class="party">
<?php
echo $adventures[1];
?>
        </p>
    </div>

    <div class="dungeon_book" style="background-image: url('green_paper.png');">

        <p class="dungeon_code">
<?php
echo $codes[2];
?>
        </p>
        <p class="dungeon_name">
<?php
echo $modules[2];
?>
        </p>
        <p class="author">
<?php
echo $authors[2];
?>
        </p>
        <p class="party">
<?php
echo $adventures[2];
?>
        </p>
    </div>


</div> <!-- class=break -->


<div class="epilogue">
Bought to you by <a href="/">mezzacotta</a><br>
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png" width="80" height="15" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported Licence</a> by The Comic Irregulars. <i>d&#109;m&#64;d&#97;nger&#109;o&#117;se&#46;n&#101;t</i><br />
<i>Hosted by: <a href="http://www.dreamhost.com/rewards.cgi?dmmaus">DreamHost</a></i>
</div> <!-- class=epilogue -->

</div> <!-- class=main -->

</div> <!-- id=page -->
</body>
</html>
