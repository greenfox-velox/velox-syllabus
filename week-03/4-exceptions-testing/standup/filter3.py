numbers = [1, 2, 3, 4, 5, 6, 7, 8]
output = []

def filter_even():
    for n in numbers:
        if n % 2 == 0:
            output.append(n)


filter_even()

print(output)
