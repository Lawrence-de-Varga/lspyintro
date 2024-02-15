obj = 'ABcd'
obj.upper() # This neither mutates nor reassigns
obj = obj.lower() # This reassigns
print(len(obj)) # This neither mutates nor reassigns
obj = list(obj) # This reassigns
obj.pop() # This mutates
obj[2] = 'X' # This mutates
obj.sort() # This mutates
set(obj) # This neither mutates nor reassigns
obj = tuple(obj) # This reassigns
