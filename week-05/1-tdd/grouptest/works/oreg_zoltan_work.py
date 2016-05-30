def anagramm(str1, str2):
    s1 = count_letters2(str1)
    s2 = count_letters2(str2)
    if s1 == s2:
        return True
    else:
        return False

def count_letters2(string):
    words = {}
    counter = 1
    if type(string) != str:
        return None
    str_sorted = string.lower()
    str_sorted = sorted(str_sorted)
    for i in str_sorted:
        if i not in words:
            words[i] = counter
        else:
            words[i] += counter
    return words

def count_letters(string):
    words = {}
    counter = 1
    if type(string) != str:
        return None
    str_sorted = string.lower()
    str_sorted = sorted(str_sorted)
    for i in str_sorted:
        if i.isalpha():
            if i not in words:
                words[i] = counter
            else:
                words[i] += counter
    return words
