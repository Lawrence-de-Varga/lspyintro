dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# Because the dict constructor create a shallow copy, the lists which are the values in the
# dict1 hash are identical not merly equal to the lists in the dict2 hash
# Therefore any change in either of them through dict1 or 
# dict2 will be reflected in both of the dicts
