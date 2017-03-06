#Running an indexing error with exception
def indexerror(value,index):
    return value[index]

#Call the indexerrr with list under indexing range and out of indexing range
x="stuff"
#Calling this will return the value
indexerror(x,3)
#Calling an out of range
indexerror(x,6)

#To overcome we can use try/catch exception method while calling
try:
    indexerror(x,6)
except IndexError:
    print("Exception occured")

#Using try not only catch exception, but can also keep the code running
def function_catch():
    try:
        indexerror(x,6)
    except IndexError:
        print('Got an exception')
    print('Still running')

#Call the function to check the indexing function
function_catch()
