ac = ['kuty', 'macsk', 'cic']
# add to all elements an 'a' on the end

# 1
i = 0
while i < len(ac):
    ac[i] += 'a'
    i += 1

print(ac)

# 2
for i in range(len(ac)):
    ac[i] += 'a'
