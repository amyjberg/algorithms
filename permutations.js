// Iterative Solution
function getPermutations(string) {
  const letters = str.split('') // yields array of all the letters
  let results = [ [letters.shift()] ] // accomplishes two things at once -- we remove the first letter from the letters array and also add it to the first array element of the results array

  // we continue looping while there are still letters we haven't shifted off of our letters array
  while(letters.length) {
    const currentLetter = letters.shift()
    const temporaryResults = []

    // our results permutations are unfinished, so we will add our current letter in at every possible position
    results.forEach(result => {
      for (let i = 0; i <= result.length; i++) {
        // we have an unfinished permutation, so let's insert our current letter
        const resultCopy = result.slice() // so we don't mutate our result!
        resultCopy.splice(i, 0, currentLetter)
        temporaryResults.push(resultCopy)
      }
    })
    results = temporaryResults // we update results to be the array of new permutations
    // if we just finished the last letter, we break out of the loop. otherwise we continue
  }
  return results.map(letterArray => letterArray.join(''))
}

// Recursive Solution -- I find it more intuitive than the iterative solution
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
