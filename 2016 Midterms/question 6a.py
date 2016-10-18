#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def readMatrix(f):
    d= {}
    nl = []
    lines = f.readlines()
    for i in lines:
        l =i.split()
        print l
    #pseduocode
        #check if string is made of alphabets. if check = TRUE
        #create dictionary key
        #the strings afterwards would be checked for numbers. if TRUE, then add in as values
        #del d[END]
        #return dictionary
        for j in l:
        if j.isdigit() == False:
                # print i
            if j not in d:
                d[j] = 1
            else:
                d[j] +=1
            return d

    # print lines

print readMatrix(open('gauss2.txt','r'))


