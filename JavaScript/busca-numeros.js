/*En una biblioteca queremos saber qué libro es el que menos páginas tiene y el que más páginas. Por suerte, no hay dos libros con el mismo número de páginas.

Necesitamos que la función reciba un array de números, sin ordenar, y que devuelva un array de dos posiciones con el índice del libro con menos páginas y el índice del libro con más páginas.*/

function minAndMaxWord(words) {
        let max = words[0]; // recuperamos el primer elemento del array
        let min = words[0];
        // recorremos el array desde el segundo elemento
        for (let i = 1, j=1; i < words.length; i++, j++) {
          // ¿es el elemento actual mayor que el máximo?
          if (words[i] > max) {
            // si es así, lo guardamos como nuevo máximo
            max = words[i]
          }
          
          if (words[j] < min) {
            // si es así, lo guardamos como nuevo máximo
            min = words[j]
          }
        }
      
        // devolvemos el máximo número que hemos encontrado
        console.log(`el numero mayor es: ${max} y el menor ${min}`);
        return [words.indexOf(min), words.indexOf(max)];
      }

const palabras = [451, 18, 23, 5, 48, 55, 88, 3111, 320];

console.log(minAndMaxWord(palabras))
