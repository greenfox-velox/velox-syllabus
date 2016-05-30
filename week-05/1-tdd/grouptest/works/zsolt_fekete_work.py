
# def only_alpha(string):
#     for letter in string:
#         if not letter in "abcdefghjklmnopqrstuvwxyzöüóőúéáű":
#     return True

def anagramm (string_first, string_second):

    string_converter_1=str(string_first)
    string_converter_2=str(string_second)
    string_1=string_converter_1.lower()
    string_2=string_converter_2.lower()
    letter_1=[]
    letter_2=[]

    for letter in range(len(string_1)):
            letter_1 +=(string_1[letter])
    for letter in range(len(string_2)):
            letter_2 += (string_2[letter])

    # if len(string_1) == 0 and len(string_2) == 0:
    #     return False

    # elif only_alpha(string_1) == False or only_alpha(string_2) == False :
    #         return False

    if (len(letter_1)==len(letter_2)):
        for letter in letter_1:
            if letter in letter_2:
                letter_2.remove(letter)
                if len(letter_2)==0:
                    return True
            else:
                return False
    else:
        return False

#Task_2
def count_letters(string_1):
    string_converter=str(string_1)
    string = string_converter.lower()
    letter_number={}
    for n in string:
        if n != ' ' or n != '*':
            for letter in string:
                letter_number[letter] = string.count(letter)
            return letter_number
        return True


    # if len(string) != 0 and only_alpha(string) == True:
