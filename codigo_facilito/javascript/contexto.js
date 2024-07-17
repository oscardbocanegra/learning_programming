let estuduante = {
    nombre: "Uriel",
    saludar: () =>{console.log("Hola soy " + this.nombre); },
    saludarAlt: function() {console.log("Hola soy " + this.nombre); }
}

estuduante.saludar(); // Hola soy undefined
estuduante.saludarAlt(); // Hola soy Uriel

// Bind, call, y apply


//CLASES

class Curso {
    constructor(titulo){
        this.titulo = titulo
    }

    inscribir(){
        console.log("Inscrito");
    }
}

let javaScript = new Curso("Curso profesional de JavaScript");

console.log(javaScript.titulo);
javaScript.inscribir()