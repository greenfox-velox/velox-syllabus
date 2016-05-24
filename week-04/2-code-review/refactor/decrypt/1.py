def decrypt(file_name):
    f = open(file_name)
    file_content = f.read()
    f.close()
    decrypted_content = ''
    
    for letter in file_content:
        if letter == ' ' or letter == '\n':            decrypted_content += letter
        else:
            decrypted_content += chr(ord(letter) - 1)

    return decrypted_content


print(decrypt('input.txt'))
