#Using time.sleep.
import _thread as thread, time

#Parallel_thread_count runs from 0 to 4 & prints the standard output
def Parallel_thread_count(myId, count):
    for i in range(count):
        time.sleep(1)
        #use Lock.acquire to lock changes
        Lock_and_release.acquire()
        print('[%s]=> %s' %(myId,i))
        #use lock.release to release lock to available.
        Lock_and_release.release()

#Make a global lock object
Lock_and_release=thread.allocate_lock()
for i in range(5):
    thread.start_new_thread(Parallel_thread_count,(i,5))
#sleep for 6 seconds
time.sleep(6)
print('Exiting Main thread')
