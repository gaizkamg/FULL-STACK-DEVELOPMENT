function averageNumber(lista) {
    let suma = 0;
    for (let numero of lista){
     suma = suma + numero;
     
    }
    totalNumeros = lista.length;
    resultadoBonito = `
    Los numeros de la lista son: ${lista} 
    En total suman: ${suma}
    y su media es de: ${suma/totalNumeros}
    `
    return console.log(resultadoBonito);
}

let lista = [1, 2, 3, 4, 5];
let lista2 = [3, 2, 5, 15, 66, 215, 7, 90];
let lista3 = [4, 40, 400, 4000, 40000];
averageNumber(lista3);
