"Enter 'exit' to stop the forking"
import os
argumentz=0

while True:
    argumentz+=1
    Process_id=os.fork()
    if Process_id==0:
        os.execlp('python','python','Sub_Tree.py', str(argumentz))
        assert False, 'error starting program'
    else:
        print('Sub_Tree is',Process_id)
        if input()=='exit': break
