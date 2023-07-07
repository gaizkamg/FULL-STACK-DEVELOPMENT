/* 

  217. Contains Duplicate
Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. */

let containsDuplicate = function (nums) {
  for (let i = 0; i <= nums.length-1; i++) {

    for (let j = i + 1; j <= nums.length-1; j++){

      if (nums[i] == nums[j]){
        return true;
      }
    }
  }

  return false
}

console.log(containsDuplicate([2,1,3,1]));