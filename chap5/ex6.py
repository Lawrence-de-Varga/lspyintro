# This function still does not print anything as the function returns before the print statement is executed

def scream(words):
    words = words + "!!!!"
    return
    print(words)

scream('Yipeee')
