<?php
$name = "David";
$isDev = true;
$age = 44;

var_dump($name);
var_dump($isDev);
var_dump($age);

gettype($name);
gettype($isDev);
gettype($age);

is_string($name);
is_bool($isDev);
is_int($age);
?>


<h1>
    <?= "Hola " . $name; ?>
</h1>

<style>
    :root {
        color-scheme: dark;
    }

    body{
        display: grid;
        place-content: center;
    }
</style>