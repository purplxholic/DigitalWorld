import math
class Point2D():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point2D(' + str(self.x) +','+str(self.y)+')'

    def add(self,v): #v would be another class
        self.x += v.dx
        self.y += v.dy
        return self

class Vector2D():
    def __init__(self,dx,dy):
        self.dx = dx
        self.dy = dy

    def length(self):
        return math.sqrt(self.dx**2 + self.dy**2)

class Polyline2D:
    def __init__(self,pt1,lista):
        #pt1 is a insgtance of Point2D
        #lista is a list of Vector2D's to add to pt1
        #[[1,2].[3,4]]
        #so i need to loop thru the length of lista, adding its vectors into pt1
        self.x = pt1.x #always updating
        self.y = pt1.y
        self.listOfVectors = [] #cos need to remember something

        for z in xrange(len(lista)):
            self.addSegment(lista[z])

    def addSegment(self,vector):
        self.listOfVectors.append(vector) #each time hv lista can add on the vector
        self.x += vector[z].dx
        self.y += vector[z].dy

    def length(self):
        summ = 0
        for x in range(len(self.listOfVectors)):
            summ+= self.listOfVectors[x].length() #from class Vector2D cos input is a variable = Vector2D
        # v = Vector2D(self.x,self.y)
        return summ

    def vertex(self,intIndex): #this is to add all the lines tgt, uncluding from (0,0)
        verteX = 1 #cheating
        verteY = 2
        
        for x in range(0,intIndex):
            verteX += self.listOfVectors[x].dx
            verteY += self.listOfVectors[x].dy
        p = Point2D(verteX,verteY)
        return p


p = Point2D(1,2)
w = Vector2D(3,4)
q = p.add(w)
print q