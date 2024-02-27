set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# set2 is a reference to the same mutable object as set1 and 
# therefore will contain everything in set1
