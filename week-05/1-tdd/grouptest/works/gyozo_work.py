def anagramm(a, b):
    if type(a) is int or type(b) is int:
        return(False)
    elif type(a) is not int or type(b) is not int:
        a = a.lower()
        b = b.lower()
        if ''.join(sorted(a)) == ''.join(sorted(b)):
            return(True)
    else:
        return(False)


def count_letters(word):
    if type(word) is int:
        return(False)
    d = {}
    n = 1
    for i in word:
        if i in d:
            d[i] += 1
        else:
            d.update({i:n})
    return d
