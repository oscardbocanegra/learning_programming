function Usuario(){
    this.id = 1
    this.recuperarCalve = function(){
        console.log('Recuperando clave...');
    }
}

let usuario = new Usuario();
console.log(usuario);