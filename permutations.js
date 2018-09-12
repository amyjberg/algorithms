/* Generating all full-length permutations of a string */

// Iterative Solution
function getPermutations(string) {


}


// Recursive Solution
function getPermutationsRec(string) {
  const permutations = []
  if (string.length === 1) {
    permutations.push(string)
  } else {
    /*
    note that if our string is empty, we bypass this loop entirely
    technically 0! is one, but here we will just return an empty
    permutations array instead of one with an empty string in it
    */
    for (let i = 0; i < string.length; i++) {
      const firstChar = string[i]
      const remainingChars = string.slice(0, i) + string.slice(i + 1)
      // we will look at the array of all permutations of the remaining characters
      getPermutationsRec(remainingChars).forEach(subPerm => {
        // we add our character at the beginning and then the permutations of the remaining characters
        permutations.push(firstChar + subPerm)
      })
    }
  }
  return permutations
}
