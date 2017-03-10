#Create a decorator using class object.
#Using initialize we creating a new method with func as name.
#Then calling the imbuilt call operator to check the results..
print('-'*50,'\n')
class decorator(object):
    def __init__(self,func):
        self.func=func
    def __call__(self, *args, **kwargs):
        #include the print to check priority
        print('Call Initiated and ran first before {}'.format(self.func.__name__))
        return self.func(*args,**kwargs)

@decorator
def printing_function():
    print('Printing function ran')

@decorator
def printing_info(name, age):
    print('Printing_info ran with arguments ({}, {})'.format(name,age))

printing_info('Baywatch',45)
printing_function()
print('-'*50,'\n')
