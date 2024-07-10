let estuduante = {
    nombre: "Uriel",
    saludar: () =>{console.log("Hola soy " + this.nombre); },
    saludarAlt: function() {console.log("Hola soy " + this.nombre); }
}

estuduante.saludar(); // Hola soy undefined
estuduante.saludarAlt(); // Hola soy Uriel