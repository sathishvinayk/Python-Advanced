#Define a class with Exception passed in
class Callback_error(Exception):
	def __init__(self,value):
		self.value=value
	#Define a str method to get the value
	def __str__(self):
		return repr(self.value)

#RUn a exception on class.
try:
	raise Callback_error(4*4)
Except Callback_error as e:
	print 'Error reported at value: ',e.value

raise Callback_error('Passing spam')
