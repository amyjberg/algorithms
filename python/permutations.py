def getPermutationsRec(string):
  permutations = []
  if len(string) == 1:
    permutations.append(string)
  else:
    for x in xrange(0, len(string)):
      firstChar = string[x]
      remainingChars = string[0:x] + string[x + 1:]
      subPermutations = getPermutationsRec(remainingChars)
      for y in xrange(0, len(subPermutations)):
        newPermutation = firstChar + subPermutations[y]
        permutations.append(newPermutation)
  return permutations
