def decrypt(file_name):
    decrypted_content = ''
    
    for letter in get_file_content(file_name):
        if not letter == ' ' or letter == '\n':
            letter = chr(ord(letter) - 1)
        decrypted_content += letter

    return decrypted_content

def get_file_content(file_name):
    f = open(file_name)
    file_content = f.read()
    f.close()
    return file_content


print(decrypt('input.txt'))
