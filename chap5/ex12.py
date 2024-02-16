# This code will raise an erro as the parameter 'first' does not hjavfe a default value 
# and was not provided with an argument when the function was called

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()
