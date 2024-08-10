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

//Alcance de propiedades

class Curso{
    #title = "JavaScript"
}

let javaScript2 = new Curso();
console.log(javaScript2.#title);


// Metodo constructor

class Curso{
    constructor(titulo, color= "Yellow"){
        this.titulo = titulo;
        this.color = color;
        console.log(arguments);
    }
}

// Herencia de clases

class User {
    constructor(name){
        this.name = name;
    }
    saludar(){console.log("Hola usuario")}
}

class Admin extends User{
    constructor(name){
        super(name);
    }

    saludar(){
        super.saludar();

        console.log("Hola soy admin")
    }
}

let admin = new Admin("David")
console.log(admin.name)



