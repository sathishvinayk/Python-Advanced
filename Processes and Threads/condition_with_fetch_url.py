#Conditions on specific threads
#Illustrating the mechanism by producer/consumer example
#Here producer adds random integers to a list at a random time and consumer retrieves those integers from list.
import threading, urllib2, time, random
class Producer(threading.Thread):
    #Produces random integers to list
    def __init__(self,integers,condition):
        threading.Thread.__init__(self)
        self.integers=integers
        self.condition=condition

    def run(self):
        #Run thread method and append random integers to integers list
        while True:
            integer=random.randint(0,256)
            self.condition.acquire()
            print('Condition acquired by %s'%self.name)
            self.integers.append(integer)
            print('%d appended to list by %s' %(integer, self.name))
            print('Condition notified by %s' %self.name)
            self.condition.notify()
            print('Condition released by %s' %self.name)
            self.condition.release()
            time.sleep(1)

class Consumer(threading.Thread):
    #Consumes random integers from a list.
    def __init__(self,integers,condition):
        threading.Thread.__init__(self)
        self.integers=integers
        self.condition=condition
    def run(self):
        #Thread run method.Consumes integers from list
        while True:
            self.condition.acquire()
            print('Condition acquired by %s'%self.name)
            while True:
                if self.integers:
                    integer=self.integers.pop()
                    print('%d popped from list by %s'%(integer, self.name))
                    break
                print 'Condition wait by %s' %self.name
                self.condition.wait()
            print('condition released by %s'%self.name)
            self.condition.release()

def main():
    integers=[]
    condition=threading.Condition()
    t1=Producer(integers, condition)
    t2=Consumer(integers, condition)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__=='__main__':
    main()
