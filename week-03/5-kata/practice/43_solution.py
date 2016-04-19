filename = 'alma.txt'
# create a function that prints the content of the
# file given in the input

def print_file(name):
    file_to_print = open(name)
    content = file_to_print.read()
    file_to_print.close()
    return content

print(print_file(filename))
