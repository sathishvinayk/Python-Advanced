#Define a class which inherits the Exception
class Inherit_Except(Exception): pass

#Create a function, calls raise with inherited class
def fun():
    raise Inherit_Except()
  
#Run a try/except to call the function
try:
    fun()
except Inherit_Except:
    print('Exception caught')
