# Write a function, that takes two strings and returns
# a boolean value based on if the two strings are Anagramms or not.
def anagramm(first_text, secound_text):
    if len(first_text) == len(secound_text):
        firstordertext = sorted(first_text)
        secoundordertext = sorted(secound_text)
        # print(firstordertext)
        # print(secoundordertext)
        if firstordertext == secoundordertext:
            return True
        else:
            return False
    else:
        return False

# firsttxt = 'almak t'
# secoundtxt = 'malakt'
#
# print(anagramm(firsttxt, secoundtxt))

# Write a function, that takes a string as an argument and returns a dictionary with all letters in
# the string as keys, and numbers as values that shows how many occurrences there are.i

def count_letters(text):
    if type(text) is int:
        return False
    else:
        newtext = sorted(text)
        # print(newtext)
        dic = {}
        n = 1
        for letters in newtext:
            if letters in dic:
                dic[letters] += 1
            else:
                dic.update({letters : n})
            # not finised yet !!!!!!!!!!!
        # print(dic)
        return dic

# sms = 'what happened'
# count_letters(sms)
