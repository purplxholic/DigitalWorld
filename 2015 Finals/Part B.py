#q3
A = [[2.2,2,3.1],[4,5,6],[7,8,9]]
total = 0.0 
def compTrace():
    total = 0.0
    for i in range(len(A)):
        total += A[i][i]
    return total
print compTrace()

#q4
def findKey(dInput,strInput):
    nl =[]
    for i in dInput:
        if strInput == dInput[i]:
            nl.append(i)
    nl.sort()
    return nl
    
print findKey({1:'singapore',20:'china',4:'japan',5:'china',10:'japan'},'china')
