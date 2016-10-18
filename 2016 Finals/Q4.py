#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

from libdw import sm

class RingCounter(sm.SM):
    count = 0
    def getNextValues(self, state,inp):
        if state == 1:
            if inp == 1:
                state = 0
                outp = '000'
            if inp == 0:
                state = 0
                outp = '000'
        if state == 0:
            nl = ['001', '010', '011', '100', '101', '110', '111']
            if inp == 0:
                for i in range(len(nl)):
                    outp = nl[i]
                    i+=1
                    RingCounter.count +=1
                    state = 0
                #outp will continue to print out the different binaryies
            if RingCounter.count == 7:
#when printed out all the different other numbers, the sm is supposed to go back to 1
                state = 0
                outp = '000'
#however once it encounters 1 again, it will witch back
            if inp == 1:
                state = 1
                outp = '000'


        return state, outp
#
print 'test 1'
r=RingCounter()
ans = r.transduce([0,0,0,0,0,0,0,0,0])
print ans==['001', '010', '011', '100', '101', '110', '111', '000', '001']
print ans 

#print 'test 2'
#r=RingCounter()
#ans = r.transduce([0,0,0,1,0,0,0,0,0])
#print ans==['001', '010', '011', '000', '001', '010', '011', '100', '101']
#
#print 'test 3'
#r=RingCounter()
#ans = r.transduce([0,0,0,1,0,0,1,0,0])
#print ans==['001', '010', '011', '000', '001', '010', '000', '001', '010']

r = RingCounter()
print r.transduce([1,0,0])