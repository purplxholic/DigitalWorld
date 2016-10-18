#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

import cmath

def norm(z1,z2,z3):
    zp1 = z1.conjugate()
    zp2 = z2.conjugate()
    zp3 = z3.conjugate()
    ans = cmath.sqrt(z1*zp1 + z2*zp2 + z3*zp3)
    # anss = ans.real()
    return round(ans.real,3)

z1 = 1 +3j
z2  = -1+3j
z3 = -1-3j
print norm(z1,z2,z3)
print z1.real