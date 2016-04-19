filename = 'alma.txt'
# create a function that reads a file and prints it's
# lines, also it should prepend an 'A' character
# to each line

# 1
def print_file_lines_with_a(name):
    file_to_print = open(name)
    content = file_to_print.read()
    file_to_print.close()
    output = ''
    lines = content.split('\n')
    for line in lines:
        output += 'a' + line + '\n'
    return output

print(print_file_lines_with_a('alma.txt'))

# 2
def print_file_lines_with_a2(name):
    file_to_print = open(name)
    lines = file_to_print.readlines()
    file_to_print.close()
    output = ''
    for line in lines:
        output += 'a' + line
    return output

print(print_file_lines_with_a2(filename))
