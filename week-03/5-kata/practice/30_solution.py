ad = [3, 4, 5, 6, 7]
# print the sum of all numbers in ad

# 1
summa = 0
i = 0
while i < len(ad):
    summa += ad[i]
    i += 1

print(summa)


# 2
summa2 = 0
for n in ad:
    summa2 += n
print(summa2)
