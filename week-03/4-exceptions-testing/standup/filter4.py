numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def filter_even(unfiltered_list):
    output = []
    for n in unfiltered_list:
        if n % 2 == 0:
            output.append(n)
    return output


output = filter_even(numbers)

print(output)
