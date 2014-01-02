
theSet = [8, 6, 7, 5, 3, 10, 9]
theGoalSum = 15

def subsetSum(theSet, theGoalSum, theSum, theSubset):
  print theSet, theSum, theSubset
  if theSum == theGoalSum:
    print theSubset
  if theSum < theGoalSum and 0 != len(theSet):
    for i in range(len(theSet)):
      nextSet = theSet[:i] + theSet[i:]
      nextSubset = theSubset[:]
      subsetSum(nextSet, theGoalSum, theSum, nextSubset)
      nextSubset.append(theSet[i])
      subsetSum(nextSet, theGoalSum, theSum + theSet[i], nextSubset)

subsetSum(theSet, theGoalSum, 0, [])
