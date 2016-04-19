names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list

def get_shortest_string_from_list(strings):
    output = strings[0]
    for string in strings:
        if len(output) > len(string):
            output = string
    return output

print(get_shortest_string_from_list(names))
