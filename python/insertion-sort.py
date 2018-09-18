def insert(sortedArray, element): # O(n) time complexity
  array = sortedArray.append(None) # we add an empty space so we can move elements over
  for x in xrange(len(sortedArray) - 1, 0, -1): # start at the biggest number after None
    if array[x] < element: # the first number we hit that is smaller than the element
      array[x + 1] = element # we insert it into the space right in front of it (which currently is None)
      break # then we break out of the loop because they rest of the elements are in the correct position
    else: # we have a number that is bigger or equal to our element
      array[x + 1] = array[x] # so we set the value to the left to be equal to it
      if x == 0: # if we got all the way to the end...
        array[0] = element # we need to insert the element at the beginning
      else:
        array[x] = None # move the 'None' over so it occupies the space that we'll scoot the next element
  return array

# function insertionSort(array) {
# 	for (let i = 1; i < array.length; i++) {
# 		const sortedSubArr = array.slice(0, i)
# 		const inserted = insert(sortedSubArr, array[i])
# 		const rest = array.slice(i + 1)
# 		array = [...inserted, ...rest]
# 	}
# 	return array
# }


