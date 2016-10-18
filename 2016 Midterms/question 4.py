#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

import math

def factors(n):
    nl = []
    # count = 1
    for count in range(1,n+1):
        if n % count == 0:
            nl.append(count)
            count +=1
    return sorted(nl)

print factors(9)
