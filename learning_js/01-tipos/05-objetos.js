let personaje = {
    nombre: "Mate",
    pelicula: "Cars",
    edad: 16,
}

console.log(personaje);
//Y si solo queremos acceder a un dato lo vamos a realizar de la siguiente manera
console.log(personaje.nombre);

//Ahora si queremos cambiar el valor de alguna propiedad lo podemos hacer de la siguiente marea
personaje.edad = 10;
console.log(personaje.edad);

// y si queremos eliminar alguna propiedad lo hacemos por meido del comando delete
delete personaje.edad;
console.log(personaje);