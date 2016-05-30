def anagramm(string_1, string_2):
    if type(string_1) != str or type(string_2) != str:
        return False

    if len(string_1) != len(string_2):
        return False

    if ' ' in string_1 or ' ' in string_2:
        return False

    if len(string_1) == 0 or len(string_2) == 0:
        return False

    return sorted(list(string_1.lower())) == sorted(list(string_2.lower()))

def count_letters(input_string):
    if type(input_string) != str:
        return False

    if len(input_string) == 0:
        return False

    else:
        letters_occurrency = {}
        for chars in input_string:
            letters_occurrency[chars] = letters_occurrency.get(chars, 0) + 1
        return letters_occurrency
