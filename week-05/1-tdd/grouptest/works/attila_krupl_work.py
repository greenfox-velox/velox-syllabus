def anagramm(string1, string2):
    if len(str(string1)) == len(str(string2)):
        list1 = list(str(string1).lower())
        list2 = list(str(string2).lower())
        if sorted(list1) == sorted(list2) and len(str(string1)) > 0:
            return True
        else:
            return False
    else:
        return False
    
def count_letters(string3):
    letter_dict = {}
    case_string = str(string3).lower()
    for i in case_string:
        if i not in letter_dict:
            letter_dict[i] = 1
        else: 
            letter_dict[i] += 1
    return letter_dict

     
