# Create a method that decrypts the texts/duplicated_chars.txt

# def decrypt(file_name):
#     f = open(file_name)
#     result = ''
#     file_lines = f.readlines()
#     f.close()
#     for line in file_lines:
#         for index in range(0, len(line), 2):
#             result += line[index]
#     return result

def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    text2 = ''
    counter = 0
    while counter != len(text):
        if text[counter] == '\n':
            text2 += text[counter]
        elif counter % 2 == 0:
            text2 += text[counter]
        counter += 1
    f.close()
    return text2

print(decrypt('../1-pip-io-modules/01_io/texts/duplicated_chars.txt'))
