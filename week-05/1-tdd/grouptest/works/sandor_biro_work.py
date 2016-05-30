def anagramm(string1, string2):
    string1_in_list = sorted(string1)
    string2_in_list = sorted(string2)
    if string1_in_list == string2_in_list:
        return True
    else:
        return False


def count_letters(string):
    new_string = sorted(string)
    my_dictionary = {}
    for i in new_string:
        my_dictionary[i] = new_string.count(i)
    return my_dictionary
