numbers = [5, 7, 9, 11, 13, 12]

i = 0
while i < len(numbers):
    if numbers[i] % 3 != 0:
        pass
    else:
        print(numbers[i])
        break
    i += 1
