#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

from libdw import sm
import copy
class Avatar:

    def __init__(self,name,hp=100,position =(1,1)):
        self.name = name
        self.hp = hp
        self.position = position

    def getName(self):
        return self.name

    def getHP(self):
        return self.hp

    def getPosition(self):
        return self.position

    def setName(self,name):
        self.name = name

    def setHP(self,hp):
        self.hp = hp

    def setPosition(self,position):
        self.position = position

    def heal(self,amount=1):
        self.amount = amount
        if self.amount > 0:
            self.hp += self.amount
        #else: #if amout of heal is less than 0
            #self.health = self.amount

    def attacked(self,amount=-1):
        self.amount = amount
        if self.amount <0:
            self.hp += self.amount #only plus since the value is alreay negative

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
            if self.world[i] =='Exit':
                return i
            else:
                return None

class DW2Game(sm.SM):

    def __init__(self,avatar,world):
        self.avatar = avatar
        self.world = world
        self.startState = (Avatar,Map)
    def getNextValues(self, state, inp):
        self.position = [0,0]
        nextState = state
        if nextState == 'move':
            if inp[0] == 'move': #to change the position
                nextState = 'move'
                if inp[1] == 'up':
                    self.position[1] += 1
                    outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()
                elif inp[1] =='down':
                    self.position[1] -= 1
                    outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()
                elif inp[1] == 'left':
                    self.position[0] -= 1
                    outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()
                elif inp[1] == 'right':
                    self.position += 1
                    outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()
            if self.world.whatisAt(tuple(self.position)) == 'Food':
                self.avatar.setHP(self.world[tuple(self.position)]) #setHP
                self.world.eatFood(tuple(self.position)) #del food
                outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()
                nextState = 'move'
            elif self.world.whatisAt(tuple(self.position)) == 'Wall':
                self.position = self.position
                outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()
                nextState = 'move'

            elif self.world.whatisAt(tuple(self.position)) == 'Enemy':
                if inp[0] == 'move':
                    self.position=self.position
                    self.avatar.setHP(self.world[tuple(self.position)]) #deduct the HP
                    outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()
                    nextState = 'move'
                else: #attack
                    nextState = 'attack'
                    outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()
            elif tuple(self.position) not in self.world: #if there is nothing
                nextState = 'move'
                outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()
            elif self.world.whatisAt(tuple(self.position)) == 'Exit':
                outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()
                return DW2Game.done()
            else:
                nextState = 'attack'
                outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()

        elif nextState == 'attack':
            if inp[0] == 'attack': #responding to attack function
                nextState = 'move'
                self.world.removeEnemy(tuple(self.position))
                outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()

            else: #if character no longer supposed to move
                nextState = 'move'
                outp = self.avatar.getName() , tuple(self.position) , self.avatar.getHP()


        return nextState, outp

    def done(self,position):
        self.position = position
        if self.world.whatIsAt[tuple(self.position)] == 'Exit':
            return True
        else:
            return False



