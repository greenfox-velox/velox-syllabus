my_file = open("texts/zen_of_python.txt", "r")

for line in my_file:
    print(line.rstrip())

my_file.close()
