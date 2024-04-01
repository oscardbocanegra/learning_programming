<?php 

// Esto es un comentario
echo "Hola, PHP \n";

/*
Este es 
un 
Comentario
*/

// variables
$my_string = "Esto es una cadena de texto";
$my_string = "Aqui cambio el valor de la cadena de texto";
echo $my_string . "\n";

echo gettype($my_string) ."\n";

$my_string = 6; // Tipado dinamico
echo($my_string)."\n";
echo gettype($my_string)."\n";

$div_info = "It's time to learn a bit of integers \n";
echo($div_info);

$my_int = 7;
echo $my_int."\n";
$my_int = $my_int + 4;
echo $my_int ."\n";
echo $my_int + 2 . "\n";
echo $my_int - 4 . "\n";

?>