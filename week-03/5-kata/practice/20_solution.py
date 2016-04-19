t = 'seasons'
out = 6
# if the last and the first letter of the string
# are the same double the variable
# called out, if not half it
if t[0] == t[len(t) - 1]:
    out *= 2
else:
    out /= 2

print(out)
