#Creating a second class which inherits the superclass

from Class_in_python import FirstClass
class SecondClass(FirstClass):
  def display(self):
      print('Current value = "%s"' %self.data)
      
#make instances
z=SecondClass()
z.setdata(42)
z.display()

