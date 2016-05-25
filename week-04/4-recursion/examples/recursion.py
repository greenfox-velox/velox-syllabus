# factorial(5) = 5 * 4 * 3 * 2 * 1

# without recursion, with iteration
def factorial_iterative(number):
    product = 1
    for i in range(number):
        product *= i+1
    return product

print('5! is', factorial_iterative(5))

# with recursion
def factorial(number):
    if number <= 1: #base case
        return 1
    else:
        return number * factorial(number-1)

print('5! is', factorial(5))
