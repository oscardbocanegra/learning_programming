function crearUsuario(name, email){
    return {
        email : email,
        name,
        activo : true,
        recuperarCave: function (){
            console.log('Recuperando clave')
        },
    };
}

let user1 = crearUsuario('David', 'davidbocanegrac@gmail.com')
let user2 = crearUsuario('Oscar', 'oscarbocanegrac@gmail.com')