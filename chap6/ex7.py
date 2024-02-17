def within_range(number):
    if (number >= 0) and (number <= 50):
        print(f"{number} is between 0 and 50.")
    elif (number > 50) and (number <= 100):
        print(f"{number} is between 51 and 100.")
    elif (number > 100):
        print(f"{number} is greater than 100.")
    else:
        print(f"{number} is less than 0.")

within_range(23)
within_range(65)
within_range(-56)
within_range(134)
