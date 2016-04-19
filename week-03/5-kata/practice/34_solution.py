numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def summa(num_list):
    s = 0
    for n in num_list:
        s += n
    return s

print(summa(numbers))
print(summa([1, 2, 3]))
