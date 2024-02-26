additional_years  = [0,10,20,30,40]

age = input("How old are you? ")

for years in additional_years:
    if years == 0:
        print(f"You are {age} years old.")
    else:
        print(f"In {years} years you will be {int(age) + years} years old.")
