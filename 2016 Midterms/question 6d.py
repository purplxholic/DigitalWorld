#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

import copy

def gaussElimination(data):
    data = readMatrix(f)
    #pseudocode
    if data[op][0][0]== 1:
        return mulRowByC(data[op][0][1],data[op][0][2],data[op][0][3])
    elif data[op][0][0] == 2:
        return addRowMulByC(data[op][0][1],data[op][0][2],data[op][0][3])
    #pseudocode
    # in the key 'op' if the index 0 of the [0] of the list = 1,


