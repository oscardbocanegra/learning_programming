/* 

&& Operador AND
|| Operador OR
! Operador de negacion o NOT
?? Operador nulish coalescing // fusion de nulos o union de nulos

*/

// CONDICIONES

let edad = 18
if (edad  >= 18){
    console.log("Eres mayor de edad")
}else{
    "Eres menor de edad"
}


// Imprimir numeros del 1 al 10 

/* 

 1. Instruccion inicial
 2. Condicion
 3. Instruccion despues de cada iteracion

*/

// FOR

for(let i = 1; i <= 10; i++){
    console.log(i);

    if(i % 2 != 0){continue;}

    console.log("Es par")
}

console.log("Hola mundo")

// WHILE

let i = 1;
while(1 < 10){
    console.log(i);
    i++;
}
