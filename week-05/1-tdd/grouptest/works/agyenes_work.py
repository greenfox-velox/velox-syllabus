def anagramm(string1, string2):
    if type(string1) != str or type(string2) != str:
        # print("not a string")
        return ""
    elif string1 == "" or string2 == "":
        # print("no empty strings please...")
        return ""
    else:
        a = list(string1.lower())
        b = list(string2.lower())
        a.sort()
        b.sort()
        if a == b:
            return True
        else:
            return False

def count_letters(string):
    if type(string) != str:
        # print("not a string")
        return ""
    d = {}
    for i in list(string.lower()):
        d[i] = d.get(i, 0) + 1
    return d

# print(count_letters("Lorem ipsum dolor sit amet, massa in pede augue, pariatur lectus lectus nostra et nonummy felis, ut justo donec, volutpat vitae donec pharetra."))
