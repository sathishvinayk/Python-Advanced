#logging on how many times, the function has ran and wat args were passed to that.
import logging,sys,time
print('-'*50,'\n')
def Generating_log(func):
    #Setting up a log file tat matches the name of the func
    logging.basicConfig(filename='{}.log'.format(func.__name__),level=logging.INFO)
    #Defing wrapitup fn, which takes args and shows on the log file
    def wrapitup(*args, **kwargs):
        logging.info(
            'Log registered with args: {}, and kwargs: {}'.format(args,kwargs)
            )
        return func(*args,**kwargs)
    return wrapitup

#Create a show_time function which shows time run.
def Show_time(func):
    def wrapitup(*args,**kwargs):
        clock_1=time.time()
        result=func(*args,**kwargs)
        clock_2=time.time()-clock_1
        print('{} got executed in: {} secs'. format(func.__name__,clock_2))
        return result
    return wrapitup

@Show_time
def printing_Show_time(name,age):
    #Assign a sleep for 1 second
    time.sleep(1)
    print('Printing show_time ran with arguments ({}, {})'.format(name,age))

@Generating_log
def printing_log(name, age):
    print('Printing_info ran with arguments ({}, {})'.format(name,age))

printing_log('Baywatch',45)
printing_Show_time('Baywatch',45)

print('-'*50,'\n')
