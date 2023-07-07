function findJavaScript(matrix) {
    const matrixx = matrix;
    for (let i=0; i < matrixx.length; i++){
      for (let j=0; j < matrixx[i].length; j++){
        if (matrixx[i][j] == 'JavaScript'){
            console.log(`La palabra JavasScript esta en la posicion:`)
          return [i, j];
        }
      }
    }
  }

  const matrix = [
    ['HTML', 'CSS', 'JavaScript'],
    ['Java', 'C++', 'Python'],
    ['Ruby', 'Go', 'Swift']
  ]
  
  const position = findJavaScript(matrix)
  console.log(position)