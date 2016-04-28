import libdw.sm as sm
class Elevator(sm.SM):
	startState ='First'

	def getNextValues(self,state,inp):
		if state == 'First':
		  if inp =='Up':
		      nextS = 'Second'
		      outp = 'Second'
		  elif inp =='Down':
		      nextS = 'First'
		      outp = 'First'

		elif state =='Second':
		  if inp=='Up':
		      nextS = 'Third'
		      outp = 'Third'
		  elif inp=='Down':
		      nextS = 'First'
		      outp = 'First'


		else:
		  if inp=='Up':
		    nextS = 'Third'
		    outp = 'Third'
		  elif inp=='Down':
		    nextS = 'Second'
		    outp = 'Second'
		return nextS, outp

                        
e = Elevator()
print e.transduce(['Up','Up','Up','Up','Down','Down','Down','Up'])


		