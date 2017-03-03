#Create a class with operator overloading method
class ThirdClass(SecondClass):                  #Inherited from secondclass
    def __init__(self,value):                   #On "ThirdClass(value)
        self.data=value
    def __add__(self,other):                    #on "self+other"
        return ThirdClass(self.data+other)
    def __str__(self):                          #On "print(self)", "str()"
        return '[ThirdClass: %s]'% self.data
    def mul(self,other):                        #In-place change: named
        self.data *= other
        
#Assign instance objects to the class, called __init__
a=ThirdClass('abc')
a.display()               #Inherited Method called

#__str__: returns display string
print(a)

#__add__: makes a new instance
b=a+'xyz'

#b has all thirdClass methods
b.display()

#__str__: returns display string
print(b)

#Mul: changes instance in place
a.mul(3)
print(a)
