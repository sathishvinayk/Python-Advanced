#Program1
#Define a class tat can generate no of calls
class TopTree:
    #Initialize a method
    def __init__(self,func):
        self.hits=0
        self.func=func
    #Make a call statement
    def __call__(self,*args):
        self.hits+=1
        print('Hits %s to %s'%(self.hits, self.func.__name__))
        return self.func(*args)
#Run a decorator on top of a def function
@TopTree
def user_method(a,b,c):
    return a+b+c

print(user_method(1,2,3))
print(user_method('a','b','c'))

#Program 2
#Nested Def functions with enclosing scope of state.
def TopTree(func):
    def hits(*args):
        hits.calls+=1
        print('call %s to %s'%(hits.calls,func.__name__))
        return func(*args)
    hits.calls=0
    return hits

#Create a customclas with decorator inside
class customClass:
    @TopTree
    def user_method(self,a,b,c): return a+b+c

X=customClass()
print(X.user_method(1,2,3))
print(X.user_method('a','b','c'))
