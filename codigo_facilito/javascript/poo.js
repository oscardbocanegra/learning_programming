// JavaScript Object Notation -> JSON

let curso = {
    titulo: "Curso profesional de JS",
    formato: "video",
    bloques: ["Introduccion", "Funciones"],
    inscribir: function(){
        console.log("Inscrito")
    }
}

curso.inscribir();

// Shorthand syntax

let nombre = "David";
let usuario = {nombre : nombre };
console.log(usuario.nombre);

// Duplicar o combinar objetos
let user = {
    edad: 20,
    nombre: "David"
}

let esquemaPermisos = {nivel: 2}

let copia = Object.assign(user, esquemaPermisos);

console.log(copia)