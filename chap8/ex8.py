text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
# The above line is searching through the string 'for the fjords', 
# not the whole string

print(text.rfind('f', 21, 35))    # 29 
# The above line is searching the entire string, between the indexes of 21 and 35


