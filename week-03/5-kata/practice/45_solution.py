filename = 'korte.txt'
# Write the numbers from 1 to 10 to the file stored in filename

output_file = open(filename, 'w')
for n in range(1, 11):
    output_file.write(str(n) + '\n')
output_file.close()

