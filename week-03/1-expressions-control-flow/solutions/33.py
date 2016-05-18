af = [4, 5, 6, 7]
# print all the elements of af

# while loop
i = 0
while i < len(af):
    print(af[i])
    i += 1

# for loop
for i in range(len(af)):
    print(i, af[i])

# function
def print_all_elements(input):
    for i in input:
        print(i)

bf = ['kutya', 'cica']

print_all_elements(af)
print_all_elements(bf)
