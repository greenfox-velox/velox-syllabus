# is_even(num) -> 'even', 'odd'

def is_even(num):
    if num % 2 == 0:
        return 'páros'
    else:
        return 'páratlan'


print(is_even(8))
