ag = [3, 4, 5, 6, 7]
# please double all the elements of the list

# while loop
i = 0
while i < len(ag):
    ag[i] *= 2
    i += 1

print(ag)

# for loop
for i in range(len(ag)):
    ag[i] *= 2

print(ag)

# double as in twice as many items
# while loop
i = 0
lenag = len(ag)

while i < lenag:
    print(ag[i])
    ag += [ag[i]]
    i += 1

print(ag)


# for loop
lenag = len(ag)

for i in range(lenag):
    ag += [ag[i]]

print(ag)
