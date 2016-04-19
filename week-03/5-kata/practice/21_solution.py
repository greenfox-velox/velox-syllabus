u = 13
# if u is between 10 and 20 print 'Sweet!'
# if less than 10 print 'More!',
# if more than 20 print 'Less!'
out = ''
if u > 10 and u <= 20:
    out = 'Sweet!'
elif u <= 10:
    out = 'More!'
else:
    out = 'Less!'

print(out)
