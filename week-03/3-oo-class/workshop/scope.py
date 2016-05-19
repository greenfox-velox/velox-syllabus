number = 1
god = 'Kronos'

print(number)

def print_n():
    name = 'Tibbor'
    god = 'Zeus'
    print(number)
    print(name)
    print('inner god', god)

print_n()
# ERRROR --> print(name)
print('outer god', god)
number = 10
print_n()
