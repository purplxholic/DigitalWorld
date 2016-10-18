#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

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

    def attacked(self,amount=-1):
        self.amount = amount
        if self.amount <0:
            self.hp += self.amount #only plus since the value is alreay negative

print 'test 1: __init__'
a=Avatar('John')
ans=(a.name, a.hp, a.position)
print ans==('John', 100, (1, 1))

print 'test 2: __init__'
a=Avatar('Jane',150,(10,10))
ans=(a.name, a.hp, a.position)
print ans==('Jane', 150, (10, 10))

print 'test 3: getName(), setName()'
a=Avatar('John')
a.setName('Jude')
ans=a.getName()
print ans=='Jude'

print 'test 4: getPosition(), setPosition()'
a=Avatar('John')
a.setPosition((1,3))
ans=a.getPosition()
print ans==(1,3)

print 'test 5: getHP(), setHP()'
a=Avatar('John')
a.setHP(200)
ans=a.getHP()
print ans==200

print 'test 6: heal()'
a=Avatar('John')
a.heal(5)
ans=a.getHP()
print ans==105

print 'test 7: attacked()'
a=Avatar('John')
a.attacked(20)
ans=a.getHP()
print ans==100

print 'test 8: heal()'
a=Avatar('John')
a.heal()
ans=a.getHP()
print ans==101

print 'test 9: attacked()'
a=Avatar('John')
a.attacked()
ans=a.getHP()
print ans==99

print 'test 10: heal(), attacked() '
a=Avatar('John')
a.attacked(2)
a.heal(-2)
ans=a.getHP()
print ans==100