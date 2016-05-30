
def anagramm(input1, input2):
    newInput1 = ''
    newInput2 = ''
    input1 = input1.lower()
    input2 = input2.lower()
    for i in input1:
        for j in input2:
            if i != j:
                pass
            else:
                newInput1 = input1.replace(i, '')
                newInput2 = input2.replace(j, '')
                input1 = newInput1
                input2 = newInput2
    if newInput1 == newInput2:
        return True
    else:
        return False

# print(anagramm('Alma', 'malas'))


def count_letters(string):
    string = string.lower()
    dictionary = {}
    for k in string:
        dictionary[k] = dictionary.get(k, 0) + 1
    return (dictionary)

# print(count_letters('alma'))
