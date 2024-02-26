def fact(n):
    product = 1

    while n > 0:
        product *= n
        n -= 1

    return product

print(fact(3))

print(fact(6))
