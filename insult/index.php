<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Mockery Most Vicious - mezzacotta</title>
<style>
img.centre {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.bg
{
    width: 1000px;
    padding: 0px;
    border: 0px;

    margin-left: auto;
    margin-right: auto;

    background-image: url('bard_2x.jpg');
    background-repeat: no-repeat;
    background-size: 1000px;
    background-position: center top;
}
.main
{
    width: 520px;
    padding-top: 10px;
    margin-left: 400px;
    margin-right: 80px;
    text-align: left;
    font-family: Arial;
}

.bard
{
    width:540px;
}

.more
{
    width:200px;
}
.marquee
{
    margin-top: 5px;
    margin-bottom: 5px;
    text-align: right;
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

p.insult
{
    width:500px;
    min-height: 44px;
    margin-top: 00px;
    margin-left: 0px;
    margin-right: 0px;
    margin-bottom: 00px;
    font-size: 20px;
    font-family: Georgia, serif;
    font-style: Italic;
    color: #663344;
    text-align: center;
}

p.more
{
    width:170px;
    min-height: 44px;
    margin-top: 00px;
    margin-left: 0px;
    margin-right: 0px;
    margin-bottom: 00px;
    font-size: 20px;
    font-family: Georgia, serif;
    font-style: Italic;
    color: #663344;
    text-align: center;
}

/* ============================================================================================================================
== BUBBLE WITH A BORDER AND TRIANGLE
** ============================================================================================================================ */

/* THE SPEECH BUBBLE
------------------------------------------------------------------------------------------------------------------------------- */

.triangle-border {
  position:relative;
  padding:15px;
  margin:1em 0 3em;
  border:5px solid black;
  color:#333;
  background:#fff;
  /* css3 */
  -webkit-border-radius:30px;
  -moz-border-radius:30px;
  border-radius:30px;
}

/* Variant : for left positioned triangle
------------------------------------------ */

.triangle-border.left {
  margin-left:0px;
}

/* Variant : for right positioned triangle
------------------------------------------ */

.triangle-border.right {
  width:170px;
  margin-left:330px; /* added width & margin-left, total = 500px */
  margin-right:30px;
}

/* THE TRIANGLE
------------------------------------------------------------------------------------------------------------------------------- */

.triangle-border:before {
  content:"";
  position:absolute;
  bottom:-20px; /* value = - border-top-width - border-bottom-width */
  left:60px; /* controls horizontal position */
  border-width:20px 20px 0;
  border-style:solid;
  border-color:black transparent;
  /* reduce the damage in FF3.0 */
  display:block;
  width:0;
}

/* creates the smaller  triangle */
.triangle-border:after {
  content:"";
  position:absolute;
  bottom:-13px; /* value = - border-top-width - border-bottom-width */
  left:67px; /* value = (:before left) + (:before border-left) - (:after border-left) */
  border-width:13px 13px 0;
  border-style:solid;
  border-color:#fff transparent;
  /* reduce the damage in FF3.0 */
  display:block;
  width:0;
}

/* Variant : left
------------------------------------------ */

/* creates the larger triangle */
.triangle-border.left:before {
  top:22px; /* controls vertical position */
  bottom:auto;
  left:-30px; /* value = - border-left-width - border-right-width */
  border-width:15px 30px 15px 0;
  border-color:transparent #000000;
}

/* creates the smaller  triangle */
.triangle-border.left:after {
  top:28px; /* value = (:before top) + (:before border-top) - (:after border-top) */
  bottom:auto;
  left:-21px; /* value = - border-left-width - border-right-width */
  border-width:9px 21px 9px 0;
  border-color:transparent #fff;
}

/* Variant : right
------------------------------------------ */

/* creates the larger triangle */
.triangle-border.right:before {
  top:22px; /* controls vertical position */
  bottom:auto;
  left:auto;
  right:-30px; /* value = - border-left-width - border-right-width */
  border-width:15px 0 15px 30px;
  border-color:transparent #000000;
}

/* creates the smaller  triangle */
.triangle-border.right:after {
  top:28px; /* value = (:before top) + (:before border-top) - (:after border-top) */
  bottom:auto;
  left:auto;
  right:-21px; /* value = - border-left-width - border-right-width */
  border-width:9px 0 9px 21px;
  border-color:transparent #fff;
}

</style>
</head>

<body bgcolor="#624E33">
<h1><img class="centre" src="MockeryMostVicious.png" width="1000" height="200" alt="Mockery Most Vicious" srcset="MockeryMostVicious_2x.png 2x"></h1>

<div class="bg">
<div class="main">

    <div class="bard">
<?php
putenv("PYTHONIOENCODING=UTF-8");
chdir('..');
$command = escapeshellcmd('/usr/bin/python3 generique.py insult/base 4');
$output = shell_exec($command);
$output = preg_replace("/'/", "’", $output);
$output = preg_replace("/&/", "&amp;", $output);
$output = preg_replace("/</", "&lt;", $output);
$output = preg_replace("/>/", "&gt;", $output);
$lines = explode("\n", rtrim($output));
foreach ($lines as $line)
{
    echo <<<EOL
        <blockquote class="triangle-border left">
            <p class="insult">
                $line
            </p>
        </blockquote>
EOL;
}
?>
    </div>

    <div class="more">
        <blockquote class="triangle-border right">
            <p class="more">
                Please sir, I want some more...<br>
<?php
$result = rand(1,20);
$src = sprintf("d20_%02d.png", $result);
$srcset = sprintf("d20_%02d_2x.png", $result);
echo "<a href=\".\"><img src=\"$src\" width=\"70\" height=\"70\" border=\"0\" alt=\"Reload\" srcset=\"$srcset 2x\" ></a>";
?>
            </p>
        </blockquote>
    </div>
    <div>
        <p>&nbsp;</p>
    </div>
</div> <!-- class=main -->
</div>

<!-- footer -->
<hr>
<p>
<i><a href="../">mezzacotta Random Generators Home</a></i>
</p>

</body>
</html>
