#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def addRowMulByC(matA,i,c,j):
    nl =[]
    nnl = []
    for k in matA[i]:
        nl.append(k*c)
    for c in range(len(matA[0])):
        nnl.append(matA[j][c]+nl[c])
    del matA[j]
    matA.insert(j,nnl)
    return matA


print addRowMulByC([[0,2,1,-1],[0,0,3,1],[0,0,0,0]],0,0.5,1)
