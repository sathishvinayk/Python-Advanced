import threading
#defining with 4 passed-in args.
class Main_Thread(threading.Thread):
    def __init__(self, LoopId, count, mutex):
        self.LoopId=LoopId
        self.count=count
        self.mutex=mutex
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('[%s]=> %s'%(self.LoopId,i))

#Use threading.lock()
Use_Lock=threading.Lock()
threads=[]
for i in range(10):
    thread=Main_Thread(i,100,Use_Lock)
    thread.start()
    threads.append(thread)

#Below thread.join waits until the thread exits
for thread in threads:
    thread.join()

print('Main thread exiting')
