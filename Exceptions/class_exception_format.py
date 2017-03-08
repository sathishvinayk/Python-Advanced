import sys
#Create some classes with nothing passed
class Top_Tree(Exception):
    pass
def Error0():
    common=Top_Tree()
    raise common

#Create the second class with Top_tree inheriting
class Branch(Top_Tree):
    pass
def Error1():
    common=Branch()
    raise common

#Create a third class with top_tree inheriting
class Leaves(Top_Tree):
    pass
def Error2():
    common=Leaves()
    raise common

#Loop over the entire list;
for func in (Error0,Error1,Error2):
    try:
        func()
    except Top_Tree:
        print('Error found: %s' %sys.exc_info()[0])
