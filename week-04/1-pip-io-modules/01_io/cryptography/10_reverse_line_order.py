in_file = open("texts/zen_of_python.txt", "r")
out_file = open("texts/reversed_zen_order.txt", "w")

original = in_file.readlines()
reversed_order = original[::-1]


for line in reversed_order:
    out_file.write(line)

in_file.close()
out_file.close()

print('ready')
