
theSet = [8, 6, 7, 5, 3, 10, 9]
theGoalSum = 15

def subsetSum(theSet, theGoalSum, theSum, theSubset):
  #print theSet, theSum, theSubset
  if theSum == theGoalSum:
    print theSubset
  if theSum < theGoalSum and 0 != len(theSet):
    first = theSet[0]
    nextSet = theSet[1:]
    nextSubset = theSubset[:]
    subsetSum(nextSet, theGoalSum, theSum, nextSubset)
    nextSubset.append(first)
    subsetSum(nextSet, theGoalSum, theSum + first, nextSubset)

subsetSum(theSet, theGoalSum, 0, [])
