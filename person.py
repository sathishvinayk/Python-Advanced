#1Start a class
class Person:
	def __init__(self,name,job=None,pay=0):
		self.name=name
		self.job=job
		self.pay=pay
	#4Encapsulate opertions for maintainability
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self,percent):
		self.pay=int(self.pay*(1+percent)) 
	#6String to present, Adding __overloading__Operators
	def __repr__(self):
		return '[Person: %s, %s]'%(self.name,self.pay)
		
#8Adding a subclass with bonus, no __init__ is present , so it inherits from Person class
class Manager:
	def giveRaise(self,percent,bonus.=10):
		Person.giveRaise(self,percent+bonus)

if __name__=='__main__':							#2 __name__When run for testing only
	bob=Person('Bob smith')							#Call a instance
	sue=Person('Sue Jones',job='dev', pay=100000)

#print(bob.name,bob.pay)
#print(sue.name,sue.pay)
	
	#7 Use repr to print the instances
	print(bob)
	print(sue)
	
#3Adding behaivors
#print(bob.name.split()[-1])
#sue.pay*=1.10
#print('%.2f' %sue.pay)
	
#5Changing hard coded values to encapsulate
#print(bob.lastName(),sue.lastName())
#sue.giveRaise(.10)
#print(sue.pay)
	
	#7Use same repr here to print sue
	print(sue)
	
	#9Create instances for Manager
	tom=Manager('Tom Jones', 'mgr',50000)
	tom.giveRaise(.10)
	print(tom.lastName())
	print(tom)
	
	#10Polymorphism in action
	print('--All three--')
	for obj in (bob,sue,tom):
		obj.giveRaise(.10)
		print(obj)
	

	
