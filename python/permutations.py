def getPermutations(string):
  letters = list(string)
  results = [[letters.pop(0)]] # start with one array with one letter in results array
  while len(letters) > 0:
    currentLetter = letters.pop(0) # decreases length of letters by one each pass through the loop
    temporaryResults = []
    for x in xrange(0, len(results)):
      for y in xrange(0, len(results[x]) + 1):
        resultCopy = results[x][:] # using slicing to get copy
        resultCopy.insert(y, currentLetter)
        temporaryResults.append(resultCopy)
    results = temporaryResults
  permutations = []
  for z in xrange(0, len(results)):
    permutations.append(''.join(results[z]))
  print(permutations)
  return permutations

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
