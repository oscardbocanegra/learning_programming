function Punto(x, y){
    this.x = x;
    this.y = y;
    this.dibujar = function(){ console.log('Dibujando...') }
}

let punto = { z: 7};
let p = Punto.call({},1,2);

console.log(punto);