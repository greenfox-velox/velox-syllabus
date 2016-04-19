ag = 'kuty'
# write a function that gets a string as an input
# and appends an 'a' character to its end

def appendA(text):
    return text + 'a'

ag = appendA(ag)

print(ag)

ag2 = ['rep', 'macsk', 'cic', 'alm', 'Ann', 'kacs']

for i in range(len(ag2)):
    ag2[i] = appendA(ag2[i])

print(ag2)

