my_file = open("texts/zen_of_python.txt", "r")

lines = my_file.readlines()

my_file.close()

# print(lines)

for line in lines:
    print(line.rstrip())
