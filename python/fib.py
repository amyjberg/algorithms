def nthFib(n):
  if n == 1:
    return 0
  else if n== 2:
    return 1
  else:
    return nthFib(n - 1) + nthFib(n - 2)

def nthFibDynamic(n):
  fibNums = {
    1: 0,
    2: 1
  }
  while len(fibNums.keys()) < n:
    newFibNum = len(fibNums.keys()) + 1
    newFib = fibNums[newFibNum - 1] + fibNums[newFibNum - 2]
    fibNums[newFibNum] = newFib
  return fibNums[n]

def nthFibOptimalSpace(n):
  fibVals = [0, 1]
  lastFibFound = 2
  if n == 1:
    return fibVals[0]
  while(lastFibFound < n):
    newFibVal = fibVals[0] + fibVals[1]
    fibVals[0] = fibVals[1]
    fibVals[1] = newFibVal
    lastFibFound += 1
  return fibVals[1]
