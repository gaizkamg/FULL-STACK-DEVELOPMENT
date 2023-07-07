var twoSum = function(nums, target) {
    const numsArr = nums;
    const targetN = target;
    
    for (let i = 0; i < numsArr.length; i++) {
      for (let j = i + 1; j < numsArr.length; j++) {
        if (numsArr[i] + numsArr[j] === targetN) {
          console.log(`Because in the array [${numsArr}] the nums ${numsArr[i]} + ${numsArr[j]} = ${targetN}, we return [${i}, ${j}]`);
          return [i, j];
        }
      }
    }
    
    console.log('No two numbers found that add up to the target.');
    return []; // Return an empty array if no pair is found
  };
  
  twoSum([2,7,11,15], 9);
   