"Enter 'exit' to stop the forking"
import os
def Main_tree():
    while True:
        newpid=os.fork()
        if newpid==0:
            Sub_Tree()
        else:
            print('Main_tree returning both ids: ', os.getpid(),newpid)
        if input()=='exit': break

def Sub_Tree():
    #os.getpid() is the unique identifier involved in fetching and displaying the process
    print('Main_tree returning Id: ', os.getpid())
    #If this is not present, we should press q more than once to stop the process.
    os._exit(0)

Main_tree()
