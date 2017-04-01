import sys
try:
    sys.exit()
except SystemExit:
    print('Ignoring Exit')   #Outputs Ingnoring exit


def second_run():
    print('Wrapping Sys world')
    sys.exit(42)
    print('This statement never reached');

if __name__=='__main__ ':
    second_run()


#Use try/catch to run again
try:
    second_run
except SystemExit:
    print('Ignored..') #Runs the entire statement without exitng

#Use try/finally to run
try:
    second_run
finally:
    print('Cleanup')  #Runs the entire statement without exitng

#################################################################
"""Using
    os._exit module
"""
def first_call():
    import os
    print("Exiting the first_call")
    os.exit(99)
    print('This is never executed')

if __name__=="__main__":
    first_call()

#Running try/catch forces to exit and except statement is never called
try:
    first_call()
except:
    print('This is never run')

#Running try/finally forces to exit and except statement is never called
try:
    first_call()
finally:
    print('This is never run')
