
# Adds a and b, returns as result
def add(a, b):
    return 5

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b:
        return a
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    return pool[int((len(pool) - 1) / 2)]

# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouéáőűöüóí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve
