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