# Preserving the decorator information from func_tools
# Use wraps from hardcoding
from functools import wraps

#Chaining two decorators in a single printing_function
import logging,sys,time
print('-'*50,'/n')
def Generating_log(func):
    #Setting up a log file tat matches the name of the func
    logging.basicConfig(filename='{}.log'.format(func.__name__),level=logging.INFO)
    #wrap the func name in @wraps
    @wraps(func)
    #Defing wrapitup fn, which takes args and shows on the log file
    def wrapitup(*args, **kwargs):
        logging.info(
            'Log registered with args: {}, and kwargs: {}'.format(args,kwargs)
            )
        return func(*args,**kwargs)
    return wrapitup

#Create a show_time function which shows time run.
def Show_time(func):
    #wrap the func name in @wraps
    @wraps(func)
    def wrapitup(*args,**kwargs):
        clock_1=time.time()
        result=func(*args,**kwargs)
        clock_2=time.time()-clock_1
        print('{} got executed in: {} secs'. format(func.__name__,clock_2))
        return result
    return wrapitup

#Add two decorators on the top of def func
@Generating_log
@Show_time
def printing_info(name,age):
    #Assign a sleep for 1 second
    time.sleep(1)
    print('Printing Info ran with arguments ({}, {})'.format(name,age))

#To make the Show_time run first wrap like the below.
printing_info=Generating_log(Show_time(printing_info))
printing_info('Baywatch',50)
print('-'*50,'\n')

#To test the wrap,Remove the stacked decorator and un comment the below and run the below line
#printing_info=Show_time(printing_info)
#print(printing_info.__name__)
#printing_info('Baywatch',50)
