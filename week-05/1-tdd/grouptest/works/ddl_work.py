# Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
#
def anagramm(str1, str2):
    a = sorted(str1)
    b = sorted(str2)

    if str1 or str2 != '':
        pass
    else:
        return('Please type in valid strings')

    try:
        if int(str1) or int(str2) == True:
            return 'Please type in words.'
        else:
            pass
    except:
        return(a == b)


# Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.

def count_letters(str3):
    try:
        if int(str3) != False:
            return 'Please type in words.'
        else:
            pass
    except:
        pass

    try:
        if str3 != '':
            pass
        else:
            return('Please type in valid strings')
    except:
        pass

    dicto = {}
    for letter in str3:
        dicto[letter] = str3.count(letter)
    return dicto

# print(count_letters('haagolemrolhianyzottazapadlaza'))
