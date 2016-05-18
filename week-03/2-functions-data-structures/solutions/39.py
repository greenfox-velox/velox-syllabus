names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list

def find_minimum(input):
    minimum_word = input[0]
    for item in input:
        if len(item) < len(minimum_word):
            minimum_word = item
    return minimum_word

print(find_minimum(names))
