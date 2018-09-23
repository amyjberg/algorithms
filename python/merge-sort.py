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

def split(list):
  mid = Math.floor(len(list) / 2)
  leftHalf = list[0:mid]
  rightHalf = list[mid:]
  return [leftHalf, rightHalf]

def mergeSort(list):
  if len(list) == 1 | len(list) == 0:
    return list
  else:
    halves = split(list)
    left = halves[0]
    right = halves[1]
    # recursive call on each half, so each half will get split into half until we get to our base case with length 1, when we will start merging them
    return merge(mergeSort(left), mergeSort(right))
