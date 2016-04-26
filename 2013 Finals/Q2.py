class Visitor():

    def __init__(self,name):
        self.name = name

    def setName(self,name):
        self.name = name

    def __call__(self,times=0):
        self.times = times 
        self.prevname = self.name
        if self.prevname == self.name:
            self.times += 1 
        return self.name + ' called the ' + str(self.times) +'th time'