# This code will raise an error as the function was called with too many arguments

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)
