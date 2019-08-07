<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>mezzacotta Café v.2.0</title>
<style type="text/css">
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

.menu_page
{
    border: 1px solid;
    padding: 15px;
    width: 900px;
    box-shadow: 5px 10px 8px #888888;
    background-color: white;
    background-image: url("background.png");
    background-position: left;
    background-size: 1041px 121px;
    border-color: #AAAAAA;
    border-spacing: 30px 30px;

}

@media
only screen and (-webkit-min-device-pixel-ratio: 2),
only screen and (   min--moz-device-pixel-ratio: 2),
only screen and (     -o-min-device-pixel-ratio: 2/1),
only screen and (        min-device-pixel-ratio: 2),
only screen and (                min-resolution: 192dpi),
only screen and (                min-resolution: 2dppx) { 
    .menu_page{
        background-image: url('background_2x.png');
        background-position: left;
        background-size: 1041px 121px;
    }
}

p.title
{
	width:700px;
    margin-top: 30px;
    margin-bottom: 10px;
    margin-left: 180px;
    margin-right: 20px;
    font-size: 30pt;
    font-family: Georgia, serif;
    color:#444444;
    text-align: right;
}

p.subtitle
{
	width:700px;
    margin-top: 10px;
    margin-bottom: 10px;
    margin-left: 180px;
    margin-right: 20px;
    font-size: 22pt;
    font-family: Arial;
    color:#46581d;
    text-align: right;
    letter-spacing: 4px;
}

p.course
{
    width:800px;
    margin-top: 50px;
    margin-bottom: 10px;
    margin-left: 200px;
    font-size: 16px;
    font-family: Arial;
    color: #46581d;
    letter-spacing: 8px;
}

p.dish
{
    width:650px;
    margin-top: 10px;
    margin-left: 230px;
    margin-bottom: 25px;
    font-size: 20px;
    font-family: Georgia, serif;
    font-style: Italic;
    color: #222222;
}

p.wine-name
{
    width:650px;
    margin-top: 10px;
    margin-left: 230px;
    margin-bottom: 5px;
    font-size: 18px;
    font-family: Georgia, serif;
    font-style: Italic;
    color: #775555;
    text-align: right;
}

p.wine-desc
{
    width:450px;
    margin-top: 10px;
    margin-left: 430px;
    margin-bottom: 0px;
    font-size: 16px;
    font-family: Georgia, serif;
    font-style: Italic;
    color: #442222;
    text-align: right;
}

p.wine-match
{
    width:680px;
    margin-top: 0px;
    margin-bottom: 5px;
    margin-left: 205px;
    font-size: 14px;
    font-family: Arial;
    color: #46581d;
    text-align: right;
    letter-spacing: 2px;
    text-transform: uppercase;
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
	#page { background: #EEEEEE; border: none; }
</style>
</head>

<body>

<div id="page">

<br class="clear">

<div class="main">

<div class="break"></div>

    <div class="menu_page">

    <p class="title">mezzacotta Café</p>
    <p class="subtitle">MENU</p>

<?php
$command = escapeshellcmd('/usr/bin/python ../generique.py dish/base dish/wine-recommend dish/wine-name dish/wine-description 5');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$lines = explode("\n", rtrim($output));
$numbers = array("ONE", "TWO", "THREE", "FOUR", "FIVE");
$n = 0;
foreach ($lines as $line)
{
    $parts = explode("~~", $line);
    $dish = trim($parts[0]);
    $winerecommend = trim($parts[1]);
    $wine = trim($parts[2]);
    $winedescription = trim($parts[3]);
    echo <<<EOL
    <p class="course">$numbers[$n]</p>
    <p class="dish">
        $dish
    </p>
EOL;
    if ($n == 3) {
        echo <<<EOL
    <p class="wine-match">$winerecommend</p>
    <p class="wine-name">
        $wine
    </p>
    <p class="wine-desc">
        $winedescription
    </p>
EOL;
    }
    $n++;
}
?>

    <div class="marquee">
        <a href="/generate/dish/"><img src="more_selections.png" srcset="more_selections_2x.png 2x" width="247" height="43" border="0" alt="More Selections">
        </a>
    </div>
    </div>

</div> <!-- class=break -->

<div class="epilogue">
Bought to you by <a href="/">mezzacotta</a><br>
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" width="80" height="15" /></a><br>
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-Noncommercial-Share Alike 4.0 International Licence</a> by The Comic Irregulars. <i>d&#109;m&#64;d&#97;nger&#109;o&#117;se&#46;n&#101;t</i>
</div> <!-- class=epilogue -->

</div> <!-- class=main -->

</div> <!-- id=page -->

<!-- footer -->
<hr>
<p>
<i><a href="../">mezzacotta Random Generators Home</a></i>
</p>

</body>
</html>
