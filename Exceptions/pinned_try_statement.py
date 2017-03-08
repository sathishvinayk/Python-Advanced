Line='-'*45+'\n'

print(Line + 'Error Catch and Exception Raised')
try:
    x='spam'[99]
except IndexError:
    print('Except Run')
finally:
    print('Finally Run')
print('After Run')

print(Line+'No Exception Raised')
try:
    x='spam'[3]
except IndexError:
    print('except Run')
finally:
    print('Finally Run')
print('After Run')

print(Line+'No Exception Raised, with ELSE')
try:
    x="spam"[3]
except IndexError:
    print('Except Run')
else:
    print('Else Run')
finally:
    print('Finally Run')
print('After Run')

print(Line+'Exception Raised But Not Caught')
try:
    x=1/0
except IndexError:
    print('Except Run')
finally:
    print('Finally Run')
print('After Run')
