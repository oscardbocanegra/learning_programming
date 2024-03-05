let obj = {};
let obj2 = new Object();

/**
 * new Array(); []
 * new String(); "" '' ``
 * new Number(); 12
 * new Boolean(); true false
*/

function Usuario(){
    this.name = "Programador feliz";
}

let user = new Usuario();
console.log(user.constructor)