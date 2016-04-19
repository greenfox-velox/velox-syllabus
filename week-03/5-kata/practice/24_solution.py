x = 8
time = 120
out = ''
# if x is dividable by 4
# and time is not more than 200
# set out to 'check'
# if time is more than 200
# set out to 'Time out'
# otherwise set out to 'Run Forest Run!'
maxtime = 200
if x % 4 == 0 and time < maxtime:
    out = 'check'
elif time >= maxtime:
    out = 'Time out'
else:
    out = 'Fussa tee fussa'

print(out)

