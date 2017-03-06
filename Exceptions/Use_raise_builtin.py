#Running an indexing error with exception
def indexerror(value,index):
    return value[index]

#Call the indexerrr with list under indexing range and out of indexing range
x="stuff"
#Calling this will return the value
indexerror(x,3)

#Try raise stament in exception
try:
    raise IndexError
except IndexError:
    print("Exception occured")

#Also we can run raise <error function on the direct shell>
raise IndexError


#
