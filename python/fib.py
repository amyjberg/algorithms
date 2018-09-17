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
