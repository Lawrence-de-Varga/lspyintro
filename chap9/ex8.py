my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

new_dict = {str: len(str) for str in my_set if (len(str) % 2 == 1)}

print(new_dict)
