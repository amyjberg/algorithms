# merge sort algorithm:
# divide into subarrays of one element
# merge every two subarrays together so they stay sorted
# continue merging every two subarrays until we just have one sorted array

def mergeSorted(listA, listB):
  pointerA = 0
  pointerB = 0
  merged = []
  while pointerA < len(listA) and pointerB < len(listB):
    # we break out of the loop once one pointer finishes its list
    print('inside while loop')
    if listA[pointerA] < listB[pointerB]:
      merged.append(listA[pointerA]) # modifies original list
      pointerA += 1
    elif listB[pointerB] < listA[pointerA]:
      merged.append(listB[pointerB])
      pointerB += 1
    else: # they are equal, so we can add and increment both
      merged = merged + [listA[pointerA], listB[pointerB]]
      pointerA += 1
      pointerB += 1
  # when we break out of the while loop, we might have some extra unmerged elements in one of the arrays
  if pointerA < len(listA):
    # we have leftover A elements to append
    return merged + listA[pointerA:]
  elif pointerB < len(listB):
    return merged + listB[pointerB:]
  else:
    # we finished both
    return merged

def mergeSort(list):
  # need to split it up into array of single-element arrays
  # then merge every two together and have new array of two-element arrays
  # then merge every two together and have new array of four-element arrays
  # continue until we're left with only one array
