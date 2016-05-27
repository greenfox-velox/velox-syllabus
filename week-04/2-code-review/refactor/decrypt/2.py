def decrypt(file_name):
    f = open(file_name)
    file_content = f.read()
    f.close()
    decrypted_content = ''
    
    for letter in file_content:
        if not (letter == ' ' or letter == '\n'):
            letter = chr(ord(letter) - 1)
        decrypted_content += letter

    return decrypted_content


print(decrypt('input.txt'))
