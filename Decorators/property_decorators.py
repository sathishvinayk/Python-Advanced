class Person:
    def __init__(self,name):
        self._name=name

    @property
    def name(self):
        "Property with name"
        print('Retrieving...')
        return self._name

    @name.setter
    def name(self,value):
        print('Setting...')
        self._name=value

    @name.deleter
    def name(self):
        print('Deleting...')
        del self._name

Tom=Person('Tom paster')
print(Tom)
Tom.name='Benjamin'
print(Tom.name)
del Tom.name

print('-'*20)
Lue=Person('Steve Jobs')
print(Lue.name)
print(Person.name.__doc__)
