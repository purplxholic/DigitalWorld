#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def mulRowByC(matA,i,c):
    nl =[]
    for k in matA[i]:
        nl.append(k*c)
    del matA[i]
    matA.insert(i,nl)
    return matA
    # return matA[i] *c
print mulRowByC([[0,2,1,-1],[0,0,3,1],[0,0,0,0]],0,2)


