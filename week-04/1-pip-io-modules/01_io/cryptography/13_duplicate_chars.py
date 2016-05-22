in_file = open("texts/zen_of_python.txt", "r")
out_file = open("texts/duplicated_chars.txt", "w")

for line in in_file:
    raw_line = line.rstrip()
    for char in raw_line:
        out_file.write(char)
        out_file.write(char)
    out_file.write("\n")

in_file.close()
out_file.close()

print('ready')
