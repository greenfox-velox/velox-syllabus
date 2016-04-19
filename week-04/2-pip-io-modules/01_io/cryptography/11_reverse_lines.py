in_file = open("texts/zen_of_python.txt", "r")
out_file = open("texts/reversed_zen_lines.txt", "w")

for line in in_file:
    line = line.rstrip()
    reversed_line = line[::-1]
    out_file.write(reversed_line + "\n")

in_file.close()
out_file.close()

print('ready')
