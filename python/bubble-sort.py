
def bubbleSort(list):
  for x in xrange(0, len(list) - 1): # we will do the entire swapping process x - 1 times
    for y in xrange(0, len(list) - 1):
      if list[y] > list[y + 1]: # we want to swap them
        bigger = list[y]
        smaller = list[y + 1]
        list[y] = smaller
        list[y + 1] = bigger
  return list
