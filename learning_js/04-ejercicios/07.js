function precioCompleto(precio, impuesto){
    precio = precio + precio * impuesto;
    return precio
}

let resultado = precioCompleto(19.90, 0.15);
console.log(resultado);