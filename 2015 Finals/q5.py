class Square:
	def __init__(self, x=0,y=0,sidelength = 1.0):
		self.x, self.y, self.sidelength = x,y, sidelength

	def getCenter(self):
		return self.x,self.y

	def getSideLength(self):
		return self.sidelength

	def containPoint(self,px,py):
		cx, cy, sLen = self.x, self.y, self.sidelength
		if abs(cx - px) <= sLen/2.0 and abs(cy - py) <= sLen/2.0: #using the distance between the centre of square relative to new point 
			return True
		else:
			return False 
	def containsquare(self, inSquare):
		x1,y1 = inSquare.x - inSquare.sidelength/2.0, inSquare.y - inSquare.sidelength/2.0
		x2,y2 = inSquare.x - inSquare.sidelength/2.0, inSquare.y + inSquare.sidelength/2.0
		x3,y3 = inSquare.x + inSquare.sidelength/2.0, inSquare.y + inSquare.sidelength/2.0
		x4,y4 = inSquare.x + inSquare.sidelength/2.0, inSquare.y - inSquare.sidelength/2.0

		if self.containPoint(x1,y1) and self.containPoint(x2,y2) and self.containPoint(x3,y3) and self.containPoint(x4,y4):
			return True
		else:
			return False

s = Square(x=1,y=1,sidelength=2.0)
print s.containPoint(1,1.5)