def indexerror(x,y):
    return x[y]

#Run a try/finally method to invoke the termination
try:
    indexerror(x,5)
finally:
    print('after fetching')

#Termination occurs even after print happends next to finally
def after():
    try:
        indexerror(x,6)  #If running within index range can return the result, for example indexerror(x,2)
    finally:
        print('After fetching')
    #Below print is ignores, since termination happend with fianlly
    print('After try statement')
