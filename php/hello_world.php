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

//$my_string = 6; // Tipado dinamico
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


$my_doble = 6.5 . "\n";
echo $my_doble;
echo gettype($my_doble)  . "\n";
echo $my_int + $my_doble  . "\n";


// booleanos
$my_bool = true;
echo $my_bool . "\n";
echo gettype($my_bool) . "\n";


echo "El valor de mi integer es $my_int y el de mi boolean es $my_bool". "\n";

//Constantes

const MY_CONSTANT = "El valor de la constante" . "\n";
echo MY_CONSTANT . "\n"; 

$my_array = [$my_string, $my_int, $my_doble];
echo gettype($my_array) . "\n";
echo $my_array[0] . "\n";
array_push($my_array, $my_bool);
print_r($my_array);
?>