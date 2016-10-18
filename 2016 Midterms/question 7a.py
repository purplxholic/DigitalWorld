#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def maxProductThree(num):
    nl = []
    count = 0
    while count < len(num):
        for i in range(len(num)):

            nl.append(num[count]*num[i])
            count +=1
    # pseudocode
    #count = fixed number. i increase. the combinations would be count * i one round, then count +=1 and repeats
    #return maximum
    return max(nl)


num = [6,-3,-10,0,2]
print maxProductThree(num)

