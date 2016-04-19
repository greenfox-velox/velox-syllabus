my_file = open("texts/zen_of_python.txt", "r")

line1 = my_file.readline()
line2 = my_file.readline()
line3 = my_file.readline()

my_file.close()

print(line1)
print(line2)
print(line3)

# print(line1.rstrip())
# print(line2.rstrip())
# print(line3.rstrip())
