dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
print(dict1 == dict2)
print(dict1 is dict2)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# The built in constructor dict creates a shallow copy, since dict1 is not nested
# dict2 is an entirely new object in memory which is equal, but not identical
# to dict1, therfore when dict2 is modified notthing changes in dict1
