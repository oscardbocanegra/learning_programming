let array = [2, 5, 7, 15, -5, -100, 55];

function getMenorMayor(arr){
    let max_value = Math.max(...arr);
    let min_value = Math.min(...arr);
    return [min_value, max_value];
}

let numeros = getMenorMayor(array);
console.log(numeros);