// Declaracion de una funcion

function saludar(){
    console.log("Hola mundo");
}

function cuadrado(numero){
    return numero * numero;
}

let cuadrado_de_dos = cuadrado(2);
console.log(cuadrado_de_dos);
console.log(cuadrado(3))


// Valores por defecto en las funciones

function saludar(apellido, nombre = ""){
    console.log(nombre, apellido)
}

saludar("Bocanegra")



/*

Scope global
Scope local

*/

nombre = "David";
function decirHola(){
    nombre = "Uriel";

console.log("Hola " + nombre);
}
decirHola();