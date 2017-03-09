#Define a class
class General:
	updated=0
	def __init__(self):
		General.updated=General.updated+1
	
	#Now define a decorator below
	@staticmethod
	def printupdated():
		print('Total number of %s class instance created" %updated)

a=General()
b=General()
c=General()
General.updated()
a.printupdated()
