# This code will raise an exception because you cannot have a parameter with no default value
# after a parameter with a default value

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
