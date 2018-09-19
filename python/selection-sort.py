
def selectionSort(list):
  for x in xrange(0, len(list)): # we loop through the array comparing at index x
    smallestVal = list[x] # set smallest to be the element at index x for now
    indexForSmallest = x
    for y in xrange(x + 1, len(list)): # now compare with every subsequent element
      if list[y] < smallestVal: # if we find a new one that's smaller we update smallestVal and indexForSmallest
        smallestVal = list[y]
        indexForSmallest = x
    # after inner loop, we know we have the smallest value, so we swap the old value at index x
    list[indexForSmallest] = list[x]
    list[x] = smallestVal # and then we put the smallest value at position x
  return list
