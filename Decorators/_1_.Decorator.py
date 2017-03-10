#Define a decorator function
#func is the function which is passed in to decorator.
#This is a decorator.
print('-'*50,'\n')
def decorator(func):
    def wrapitup():
        return func()          #Execute the func function
    return wrapitup   #waiting to be executed

def printing_function():
    print('Printing function ran')

decorated_print=decorator(printing_function)
decorated_print()
print('-'*50,'\n')


#Display the priority of functions by adding a print to check
#which function ran first
def decorator(func):
    def wrapitup():
        #include the print to check priority
        print('WraptitUP function ran first before {}'.format(func.__name__))
        return func()          #Execute the func function
    return wrapitup   #waiting to be executed

def printing_function():
    print('Printing function ran')

decorated_print=decorator(printing_function)
decorated_print()
print('-'*50,'\n')


#Implement the @ decorator to call explicitly
#And call the printing_function directly
def decorator(func):
    def wrapitup():
        #include the print to check priority
        print('WraptitUP function ran first before {}'.format(func.__name__))
        return func()          #Execute the func function
    return wrapitup   #waiting to be executed

@decorator              #Use @symbol decorator to implement all dec functionalities
def printing_function():
    print('Printing function ran')

printing_function()    #Simply call printing_function
print('-'*50,'\n')


#Running two different functions with main decorator.
#To do so we need to include the main decorator on both functions
#if we run printing_info with two arguments, it throws an eror
#So in order to make it run, we need to include **kargs, *args to WraptitUP function
def decorator(func):
    def wrapitup(*args,**kwargs):
        #include the print to check priority
        print('WraptitUP function ran first before {}'.format(func.__name__))
        return func(*args,**kwargs)      #Include the args to run more than one argument.
    return wrapitup   #waiting to be executed

@decorator
def printing_function():
    print('Printing function ran')

@decorator
def printing_info(name, age):
    print('Printing_info ran with arguments ({}, {})'.format(name,age))

printing_info('Baywatch',45)
printing_function()
print('-'*50,'\n')
