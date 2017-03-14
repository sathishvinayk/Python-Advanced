#Using a time.sleep to pause the calling process for number of secodns
#Each count counts up to same stdout stream.
#Forks copy memory, including file descriptors.
import os,time

def counter(count):
    for i in range(count):
        time.sleep(1)
        print('[%s]=> %s' %(os.getpid(),i))

for i in range(5):
    pid=os.fork()
    if pid!=0:
        print('Process %d spawed' %pid)
    else:
        counter(5)
        os._exit(0)

print('Main process exiting')
