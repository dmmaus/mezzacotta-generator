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
    margin-left: auto;
    margin-right: auto;
    text-align: left;
    font-family: Arial;
    height: 1800px;
}

.dungeon_book
{
    width: 900px;
    box-shadow: 5px 10px 8px #00000088;
    border-spacing: 30px 30px;
}

img.dungeon_illustration
{
    margin-top: 10px;
    margin-bottom: 200px;
    margin-left: 75px;
    margin-right: 75px;
    border: 5px solid #ffffff;
    width: 750px;
    height: 300px;
    object-fit: cover;
}

p.dungeon_code
{
	width:700px;
    margin-top: 10px;
    margin-bottom: 5px;
    margin-left: 100px;
    margin-right: 100px;
    font-size: 18pt;
    font-family: ddFont;
    color:white;
    text-align: center;
    padding: 10px;
}

p.dungeon_stripe
{
    width: 160px;
    margin-top: 10px;
    margin-bottom: 5px;
    margin-left: 10px;
    margin-right: 50px;
    font-size: 10pt;
    font-family: ddFont;
    color: black;
    text-align: center;
    position: absolute;
    transform: translate(-16px, 40px) rotate(-45deg);
}

p.dungeon_corner
{
    width: 50px;
    margin-top: 10px;
    margin-bottom: 5px;
    margin-left: 10px;
    margin-right: 50px;
    font-size: 14pt;
    font-family: ddFont;
    color:white;
    text-align: left;
    position: absolute;
}

p.dungeon_name
{
	width:600px;
    margin-top: 0px;
    margin-bottom: 15px;
    margin-left: 150px;
    margin-right: 150px;
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
    margin-left: 200px;
    margin-right: 200px;
    font-size: 14pt;
    font-family: ddFont;
    color:white;
    text-align: center;
}

p.party
{
	width:600px;
    margin-top: 20px;
    margin-bottom: 20px;
    margin-left: 150px;
    margin-right: 150px;
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
<link rel="shortcut icon" href="https://www.mezzacotta.net/wp/wp-content/themes/mezzacotta/favicon.ico" />
<link rel="stylesheet" href="https://www.mezzacotta.net/wp/wp-content/themes/mezzacotta/style.css" type="text/css" media="screen" />

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
$command = escapeshellcmd('/usr/bin/python3 generique.py dungeon/code 5');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$codes = explode("\n", rtrim($output));

$command = escapeshellcmd('/usr/bin/python3 generique.py dungeon/stripe 5');
$output = shell_exec($command);
$output = strtoupper($output);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$stripes = explode("\n", rtrim($output));

$command = escapeshellcmd('/usr/bin/python3 generique.py dungeon/module 5');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$modules = explode("\n", rtrim($output));

$command = escapeshellcmd('/usr/bin/python3 generique.py dungeon/attribution 5');
$output = shell_exec($command);
$output = preg_replace("/By /", "by ", $output);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$authors = explode("\n", rtrim($output));

$command = escapeshellcmd('/usr/bin/python3 generique.py dungeon/adventure 5');
$output = shell_exec($command);
$output = strtoupper($output);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$adventures = explode("\n", rtrim($output));

$papers = array("red", "blue", "green", "orange", "purple");
shuffle($papers);

$arts = array();
for ($i = 1; $i <= 18; $i++)
{
    $arts[] = sprintf("%02d", $i);
}
shuffle($arts);

$angles = array();
for ($i = 0; $i < 5; $i++)
{
    $angles[] = strval(rand(-20, 20) / 10.0);
}
?>

<?php echo "<div class=\"dungeon_book\" style=\"background-image: url('" . $papers[0] . "_paper.png'); transform: translate(0px, -0px) rotate(" . $angles[0] . "deg);\">"; ?>

        <p class="dungeon_corner">
<?php echo $codes[0]; ?>
        </p>
        <p class="dungeon_stripe">
<?php echo $stripes[0]; ?>
        </p>
        <p class="dungeon_code">
<?php echo "Dungeon Module " . $codes[0]; ?>
        </p>
        <p class="dungeon_name">
<?php echo $modules[0]; ?>
        </p>
        <p class="author">
<?php echo $authors[0]; ?>
        </p>
        <p class="party">
<?php echo $adventures[0]; ?>
        </p>

<?php echo '<img class="dungeon_illustration" src="art_' . strval($arts[0]) . '.png">'; ?>

    </div>

<?php echo "<div class=\"dungeon_book\" style=\"background-image: url('" . $papers[1] . "_paper.png'); transform: translate(0px, -480px) rotate(" . $angles[1] . "deg);\">"; ?>

        <p class="dungeon_corner">
<?php echo $codes[1]; ?>
        </p>
        <p class="dungeon_stripe">
<?php echo $stripes[1]; ?>
        </p>
        <p class="dungeon_code">
<?php echo "Dungeon Module " . $codes[1]; ?>
        </p>
        <p class="dungeon_name">
<?php echo $modules[1]; ?>
        </p>
        <p class="author">
<?php echo $authors[1]; ?>
        </p>
        <p class="party">
<?php echo $adventures[1]; ?>
        </p>

<?php echo '<img class="dungeon_illustration" src="art_' . strval($arts[1]) . '.png">'; ?>

    </div>

<?php echo "<div class=\"dungeon_book\" style=\"background-image: url('" . $papers[2] . "_paper.png'); transform: translate(0px, -960px) rotate(" . $angles[2] . "deg);\">"; ?>

        <p class="dungeon_corner">
<?php echo $codes[2]; ?>
        </p>
        <p class="dungeon_stripe">
<?php echo $stripes[2]; ?>
        </p>
        <p class="dungeon_code">
<?php echo "Dungeon Module " . $codes[2]; ?>
        </p>
        <p class="dungeon_name">
<?php echo $modules[2]; ?>
        </p>
        <p class="author">
<?php echo $authors[2]; ?>
        </p>
        <p class="party">
<?php echo $adventures[2]; ?>
        </p>

<?php echo '<img class="dungeon_illustration" src="art_' . strval($arts[2]) . '.png">'; ?>

    </div>

<?php echo "<div class=\"dungeon_book\" style=\"background-image: url('" . $papers[3] . "_paper.png'); transform: translate(0px, -1440px) rotate(" . $angles[3] . "deg);\">"; ?>

        <p class="dungeon_corner">
<?php echo $codes[3]; ?>
        </p>
        <p class="dungeon_stripe">
<?php echo $stripes[3]; ?>
        </p>
        <p class="dungeon_code">
<?php echo "Dungeon Module " . $codes[3]; ?>
        </p>
        <p class="dungeon_name">
<?php echo $modules[3]; ?>
        </p>
        <p class="author">
<?php echo $authors[3]; ?>
        </p>
        <p class="party">
<?php echo $adventures[3]; ?>
        </p>

<?php echo '<img class="dungeon_illustration" src="art_' . strval($arts[3]) . '.png">'; ?>

    </div>

<?php echo "<div class=\"dungeon_book\" style=\"background-image: url('" . $papers[4] . "_paper.png'); transform: translate(0px, -1920px) rotate(" . $angles[4] . "deg);\">"; ?>

        <p class="dungeon_corner">
<?php echo $codes[4]; ?>
        </p>
        <p class="dungeon_stripe">
<?php echo $stripes[4]; ?>
        </p>
        <p class="dungeon_code">
<?php echo "Dungeon Module " . $codes[4]; ?>
        </p>
        <p class="dungeon_name">
<?php echo $modules[4]; ?>
        </p>
        <p class="author">
<?php echo $authors[4]; ?>
        </p>
        <p class="party">
<?php echo $adventures[4]; ?>
        </p>

<?php echo '<img class="dungeon_illustration" src="art_' . strval($arts[4]) . '.png" style="margin-bottom: 20px;">'; ?>

    </div>

</div> <!-- class=main -->

<div class="epilogue">
Bought to you by <a href="/">mezzacotta</a><br>
<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png" width="80" height="15" /></a><br />This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported Licence</a> by The Comic Irregulars. <i>d&#109;m&#64;d&#97;nger&#109;o&#117;se&#46;n&#101;t</i><br />
<i>Hosted by: <a href="https://www.dreamhost.com/rewards.cgi?dmmaus">DreamHost</a></i>
</div> <!-- class=epilogue -->

</div> <!-- id=page -->
</body>
</html>
