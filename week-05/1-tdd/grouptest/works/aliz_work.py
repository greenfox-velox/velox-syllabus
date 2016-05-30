# Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.

def anagramm(string1, string2):
    if type(string1) == int:
        return False

    if string1 == '' or string2 == '':
        return False

    if len(string1) != len(string2):
        return False

    char_list1 = []
    for char1 in string1:
        char_list1 += char1.lower()

    char_list2 = []
    for char2 in string2:
        char_list2 += char2.lower()

    if sorted(char_list1) != sorted(char_list2):
        return False
    return True

# print(anagramm('alma', 'lamm'))
# print(anagramm('', ''))
# print(anagramm('123', '321'))
# print(anagramm(123, 321))


# Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.

def count_letters(string):
    string = str(string)
    string = str(string.lower())
    letters_in_string = {}
    for letter in string:
        letters_in_string[letter] = string.count(letter)
    return letters_in_string

# print(count_letters('alma'))
# print(count_letters(''))
# print(count_letters('Alma'))
# print(count_letters(123))
