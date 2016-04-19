def is_fizzish(number, base):
    return number % base == 0 or str(base) in str(number)

def fizz_buzz(minimum, maximum = 100):
    print(kutyaaa)
    fizz_number = 3
    buzz_number = 5
    n = minimum
    while n <= maximum:
        if is_fizzish(n, fizz_number) and is_fizzish(n, buzz_number):
            print('fizzbuzz')
        elif is_fizzish(n, buzz_number):
            print('buzz')
        elif is_fizzish(n, fizz_number):
            print('fizz')
        else:
            print(n)
        n += 1



fizz_buzz(1, 100)







def is_big_number(number):
    return number > 100

def dude_gonna_tell_bout_bigness(number):
    print('I\'m gon decide on:')
    print(number)
    if is_big_number(number):
        print('Dat is sooo big!')
    else:
        print('WTF is dat man?')


# usage: dude_gonna_tell_bout_bigness(5)
















