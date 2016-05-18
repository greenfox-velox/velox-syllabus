ah = ['kuty', 'macsk', 'cic']
# add to all elements an 'a' on the end

# while loop
i = 0
while i < len(ah):
    # print(ah[i]+'a')
    ah[i] += 'a'
    i += 1

print(ah)

# for loop 1
for allat in ah:
    print(allat+'a')

# for loop 2
for i in range(len(ah)):
    ah[i] += 'a'

print(ah)
