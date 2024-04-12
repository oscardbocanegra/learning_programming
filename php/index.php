<?php
$name = "David";
$isDev = true;
$age = 20;

//TYPES

// var_dump($name);
// var_dump($isDev);
// var_dump($age);

// gettype($name);
// gettype($isDev);
// gettype($age);

// is_string($name);
// is_bool($isDev);
// is_int($age);

$output = "Hola \"$name\", con una edad de $age";

//CONSTANTES
const NOMBRE = "Oscar";  
?>


<h1>
    <?= $output; ?>
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