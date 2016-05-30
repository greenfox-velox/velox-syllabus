# Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
def anagramm(string_first, string_second):
    string1 = str(string_first)
    string2 = str(string_second)
    if string1 == '' or string2 == '':
        return False
    elif len(string1) != len(string2):
        return False
    else:
        sorted_first_string = sorted(string1.lower())
        sorted_second_string = sorted(string2.lower())
        if sorted_first_string == sorted_second_string:
            return True
        else:
            return False


# Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys,
#and numbers as values that shows how many occurrences there are.
def count_letters(string_input):
    string = str(string_input)
    letters = {}
    for i in string.lower():
        letters[i] =  (string.lower()).count(i)
    return letters
