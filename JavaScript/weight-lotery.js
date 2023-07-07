/*     const weight = {
        green : 10,
        yellow : 20,
        red : 30,
        black : 35
    }

    const totalWeightArray = Object.values(weight);
    const totalWeight = totalWeightArray.reduce(
        (accumulator, currentValue) => accumulator + currentValue
    );

    const randomNumber = Math.random() * totalWeight;
    console.log(`The random number is: ${randomNumber}`);

    for (let weightNum in weight){
        let winner = Object.keys(weight);
        console.log(weight[weightNum], winner, );
        if (weight[weightNum] >= randomNumber){
            
            return console.log(`The winner is... ${weightNum}`);
        }
        else{
            console.log('The lotery continue...')
        }
        
    } */
/*     function weightedLottery(weight) {
        const totalWeightArray = Object.values(weight);
        const totalWeight = totalWeightArray.reduce(
            (accumulator, currentValue) => accumulator + currentValue
        );
    
        const randomNumber = Math.random() * totalWeight;
        console.log(`The random number is: ${randomNumber}`);
        let cumulativeWeight = 0;
        for (let weightNum in weight) {
            if (weight.hasOwnProperty(weightNum)) {
                cumulativeWeight += weight[weightNum];
                if (randomNumber < cumulativeWeight) {
                    return `The winner is... ${weightNum}`;
                }
            }
        }
    

    }
    
    const weight = {
        green: 10,
        yellow: 20,
        red: 30,
        black: 135
        const winner = weightedLottery(weight);
        console.log(winner);
    }; */


/*    function weightedLottery(items) {
       // Create an array to store the weighted items
       const weightedItems = [];
     
       // Iterate over each item in the items object
       for (let item in items) {
         // Get the weight of the current item
         const weight = items[item];
     
         // Add the item to the weightedItems array multiple times based on its weight
         for (let i = 0; i < weight; i++) {
           weightedItems.push(item);
         }
       }
     
       // Randomly select an item from the weightedItems array
       const randomIndex = Math.floor(Math.random() * weightedItems.length);
       const selectedItem = weightedItems[randomIndex];
     
       return selectedItem;
     } */


/* function weightedLottery(weight) {
    const totalWeightArray = Object.entries(weight);
    const totalWeight = totalWeightArray.reduce(
        (accumulator, [, currentValue]) => accumulator + currentValue, 
        0
    );

    const randomNumber = Math.random() * totalWeight;
    console.log(`randomNumber: ${randomNumber} totalWeight:${totalWeight}`);
    let cumulativeWeight = 0;
    for (let weightNum in weight) {
        console.log(`cumulativeWeight: ${cumulativeWeight}`);
        
            cumulativeWeight += weight[weightNum];
            if (randomNumber <= cumulativeWeight) {
                return `The winner is... ${weightNum}`;
            }
      
    }
} */


 /*  function weightedLottery(items, veces) {
    if (typeof items !== 'object' || Array.isArray(items)) {
      throw new Error('Items must be an object.');
    }
  
    for (let i = 1; i <= veces; i++) {
      // Convert the object to an array of [name, weight] pairs
      const itemsArray = Object.entries(items);
  
      // Calculate the total weight
      const totalWeight = itemsArray.reduce((accumulator, [, weight]) => accumulator + weight, 0);
  
      // Generate a random number between 0 and totalWeight
      const randomNumber = Math.random() * totalWeight;
  
      // Iterate over the items and determine the selected item
      let cumulativeWeight = 0;
  
      for (const [name, weight] of itemsArray) {
        cumulativeWeight += weight;
        if (randomNumber < cumulativeWeight) {
          console.log(`The winner in the ${i}th   iteration is: ${name}`);
          break; // Break out of the loop once a winner is determined
        }
      }
    }
  } */
/*   
  const weightedLottery = (weights, veces) => {

  
    for (let i = 1; i <= veces; i++) {
    // keep track of your  weights
    // ['green', 'yellow', 'yellow', 'red', 'red', 'red']
    let containerArray = [];

    Object.keys(weights).forEach(key =>{
        for (let i = 0; i < weights[key]; i++) {
            containerArray.push(key);
        }
    })
    let win = containerArray[(Math.random() * containerArray.length) | 0];
    console.log(win);
    };
  };

const weights = {
  winning: 1,
  losing: 1000
}

weightedLottery(weights, 1000); */

const weightedLottery = (weights, numPartidas) => {
  const entries = Object.entries(weights);
  const totalWeight = entries.reduce((sum, [, weight]) => sum + weight, 0);
  
  for (let partida = 1; partida <= numPartidas; partida++) {
    let randomNumber = Math.random() * totalWeight;
    let winner = null;

    for (const [item, weight] of entries) {
      if (randomNumber < weight) {
        winner = item;
        break;
      }
      randomNumber -= weight;
    }

    console.log(`Partida ${partida}: El ganador es ${winner}`);
  }
};

const weights = {
  black: 100,
  green: 1,
  yellow: 2,
  red: 3,
};

const numPartidas = 100;
weightedLottery(weights, numPartidas);