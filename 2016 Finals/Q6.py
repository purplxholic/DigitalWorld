#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

import copy

class Map:
    def __init__(self,world):
        self.world = world #a dictionary

    def whatIsAt(self,x):
        self.x = x
        if self.x not in self.world:
            return 'Empty'
        else:
            if self.world[self.x] == 'x':
                return 'Exit'
            elif self.world[self.x] == 0:
                return 'Wall'
            elif self.world[self.x] > 0:
                return 'Food'
            elif self.world[self.x] < 0:
                return 'Enemy'
        

    def getEnemyAttack(self,position):
        self.position = position
        if self.position not in self.world:
            return False
        else:
            return self.world[self.position]

    def getFoodEnergy(self,position):
        self.position = position
        if self.position not in self.world:
            return False
        else:
            return self.world[self.position]

    def removeEnemy(self,position):
        self.position = position
        if self.position not in self.world:
            return False
        else:
            if self.world[self.position] < 0:
                del self.world[self.position]
                return True
            else:
                return False

    def eatFood(self,position):
        self.position = position
        if self.position not in self.world:
            return False
        else:
            if self.world[self.position] > 0:
                del self.world[self.position]
                return True
            else:
                return False

    def getExitPosition(self):
        for i in self.world:
            if self.world[i] == 'x':
                return i
            else:
                return None

world={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0, (5,0): 0,(0,1):0, (1,1): 2, (2,1):-3, (5,1): 0,(0,2):0, (5,2): 0,(0,3):0, (5,3): 0,(0,4):0, (5,4): 0,(0,5):0, (1,5):0 , (2,5):0, (3,5): 0, (4,5):'x', (5,5): 0}

print 'test 1: object instantiation'
m=Map(world)
print m.world=={(3, 0): 0, (2, 1): -3, (5, 1): 0, (2, 5): 0, (0, 3): 0, (4, 0): 0, (5, 5): 0, (1, 5): 0, (5, 0): 0, (0, 4): 0, (5, 3): 0, (1, 1): 2, (5, 4): 0, (0, 0): 0, (4, 5): 'x', (0, 5): 0, (1, 0): 0, (3, 5): 0, (0, 1): 0, (2, 0): 0, (5, 2): 0, (0, 2): 0}

print 'test 2: whatIsAt'
print m.whatIsAt((1,0))=='Wall'

print 'test 3: whatIsAt'
print m.whatIsAt((2,1))=='Enemy'

print 'test 4: whatIsAt'
print m.whatIsAt((1,1))=='Food'

print 'test 5: getFoodEnergy'
w1=m.getFoodEnergy((1,1))
w2=m.getFoodEnergy((3,3))
print (w1,w2)==(2, False)

print 'test 6: getEnemyAttack'
w1=m.getEnemyAttack((2,1))
w2=m.getEnemyAttack((3,3))
print (w1,w2)==(-3, False)

print 'test 7: removeEnemy'
w1=m.getEnemyAttack((2,1))
w2=m.removeEnemy((2,1))
w3=m.getEnemyAttack((2,1))
print (w1,w2,w3)==(-3, True, False)

print 'test 8: whatIsAt'
print m.whatIsAt((1,4))=='Empty'

print 'test 9: getFoodEnergy'
print m.getFoodEnergy((1,4))==False

print 'test 10: getEnemyAttack'
print m.getEnemyAttack((1,4))==False

print 'test 11: whatIsAt'
print m.whatIsAt((4,5))=='Exit'

print 'test 12: getExitPosition'
print m.getExitPosition()==(4,5)

print 'test 13: eatFood'
w1=m.whatIsAt((1,1))
w2=m.eatFood((1,1))
w3=m.whatIsAt((1,1))
print (w1,w2,w3)==('Food',True,'Empty')

print 'test 14: test aliasing'
ans= m.world == world 
print ans==False
