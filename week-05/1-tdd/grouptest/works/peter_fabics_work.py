def anagramm(x, y):
    x = x.upper()
    y = y.upper()
    if sorted(x) == sorted(y):
        return True
    else:
        return False

def count_letters(string):
    d = {}
    for w in string:
        d[w] = string.count(w)
    for k in sorted(d):
        return d
        #print (k + ' x ' + str(d[k]))
