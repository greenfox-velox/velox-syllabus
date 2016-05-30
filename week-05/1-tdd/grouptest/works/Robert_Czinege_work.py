def anagramm(string1, string2):
    if len(str(string1)) != len(str(string2)):
        return False
    else:
        if ''.join(sorted(str(string1).lower())) == ''.join(sorted(str(string2).lower())):
            return True
        else:
            return False

def count_letters(input_string):
    character_dictionary = {}
    for i in str(input_string).lower():
        if i not in character_dictionary:
            character_dictionary[i] = str(input_string).lower().count(i)
        else:
            pass
    return character_dictionary
