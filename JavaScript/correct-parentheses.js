/* Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
 */
/**
 * @param {string} string
 * @return {boolean}
 */
const isValid = function(string){
   const stack = [];
   const openingPar = ['(', '{', '['];
   const closingPar = [')', '}', ']'];

   for (let i; i <= string.length; i++){
      const char = string[i];
      if (char )
   }

}    



string = "()]{}"
console.log(isValid(string));