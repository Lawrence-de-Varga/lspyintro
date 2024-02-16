# This code produces a NameError because the variable foo is 
# local to the function set_foo and thus cannot be referenced outside ofg the function body.

def set_foo():
    foo = 'bar'

set_foo()
print(foo)
