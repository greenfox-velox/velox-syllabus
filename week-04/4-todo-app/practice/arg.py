import sys

print(sys.argv)
if (len(sys.argv) == 1):
    print('No arguments :(')
elif (sys.argv[1] == 'add'):
    print('Added todo elem: ' + sys.argv[2])
else:
    print('nem is kacsa')
