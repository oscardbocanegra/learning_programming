<?php
$name = "David";
$isDev = true;
$age = 60;

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
$output_age = match (true) {
    $age < 2 => "Eres un bebé $name",
    $age < 10 => "Eres un niño $name",
    $age < 18 => "Eres un adolescente $name",
    $age == 18 => "Eres mayor de edad $name",
    $age < 50 => "Eres un adulto joven $name",
    $age >= 50 => "Eres un adulto mayor $name",
    default => "Ya eres más adulto que todos $name"
};

$bestLanguages = ["PHP", "JavaScript", "Python"];
$bestLanguages[] = "Java";
$bestLanguages[] = "TypeScript";

//CONSTANTES
//const NOMBRE = "Oscar";  
?>

<ul>
    <?php foreach($bestLanguages as $languege) : ?>
        <li> <?= $languege ?> </li>
    <?php endforeach ?>
</ul>


<h1>
    <?= $output; ?>
</h1>

<h2>
<?= $output_age; ?>
</h2>

<h3>
    El mejor lenguaje es <?=  $bestLanguages[4] ?>
</h3>

<style>
    :root {
        color-scheme: dark;
    }

    body{
        display: grid;
        place-content: center;
    }
</style>