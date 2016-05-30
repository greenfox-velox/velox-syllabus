# Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.

def anagramm(s1, s2):
    s1 = str(s1.lower())
    s2 = str(s2.lower())
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


# Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.

def count_letters(string):
    string = str(string.lower())
    dicts = {}
    for letter in string:
        dicts[letter] = string.count(letter)
    return dicts
