class FirstClass:
  def setdata(self,value):
      self.data=value
  def display(self):
      print(self.data)
      
#Creating multiple instance
x=FirstClass()
y=FirstClass()

#Assigning or setting data to the class object
x.setdata('Bob arthur')
y.setdata(1.344)

#Calling display method
x.display()
y.display()

#Assinging a explicit instance object.
x.data="New Value"
x.display()

#Generating a new attribute which is entirely new namespace
x.anothername="spam"
