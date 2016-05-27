# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

def sum(number):
    if (number < 10):
        return number
    else:
        last_digit = number % 10
        rest_of_num = number // 10
        return last_digit + sum(rest_of_num)

print(sum(12345))
