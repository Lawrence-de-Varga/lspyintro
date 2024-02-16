# This code prints 'bar' as the global variable foo is not the same as the local variable 
# cdreated in the body of the set_foo function


foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)
