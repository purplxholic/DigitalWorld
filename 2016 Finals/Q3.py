#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.
import sys
def maxOccurrences(inp):
    new = inp.split()
    d = {}

    for i in new:
        if i in d:
            d[i]+= 1
        else:
            d[i] = 1

    currentmax = -sys.maxint
    for i in d.values():
        if i> currentmax:
            currentmax = i

    maxList = []
    for k,v in d.items():
        if v == currentmax:
            maxList.append(int(k)) #change to integer output
            times = d[k]
    return sorted(maxList), times

print 'test 1'
inp='2 3 40 3 5 4 -3 3 3 2 0'
ans = maxOccurrences(inp)
print ans==([3], 4)