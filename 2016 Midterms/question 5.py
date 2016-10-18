#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def combinations(n1,n2):
    nl = []
    nnl =[]
    if n1 == 0 and n2 == 0:
        nl.append([])
        nl.append(0)
        return nl
    else:
        for i in range(n1,n2):
            for j in range(n1+1,n2+1):
                if i != j and i < j:
                    nl.append((i,j))
        length = len(nl)
        nnl = nl
        nnl.append(length)
        return nnl

print combinations(3,5)
