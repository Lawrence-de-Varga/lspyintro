my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)


def find_integers(lst):
    return [element for element in lst if (type(element) is int)]


intergers = find_integers(my_tuple)

print(intergers)
