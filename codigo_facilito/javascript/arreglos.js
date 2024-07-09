let calificaciones = [10,10,5,9,7,9]

let arreglo = [1,2,3,4,5];

for(let i = 0; i<arreglo.length; i++){
    let elemento = arreglo[i];

    console.log(elemento)
}

// FOREACH

let lenguajes = ["JavaScript", "Python", "Java"];

lenguajes.forEach(function(lenguaje){console.log(lenguaje);})

//Reducir un arreglo a solo un elemento

let nombres = ["David", "Bocanegra"];

let html = nombres.reduce(function(acc, nombre){
    return acc + "<li>" + nombre + "</li>"
})

console.log(html);