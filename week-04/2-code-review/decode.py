# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt_char(char):
    return chr(ord(char)-1)

def is_whitespace(char):
    return char in "\n "

def decrypt(file_name):
    f = open(file_name)
    result = f.read()
    f.close()

    output_text = ""

    for character in result:
        if is_whitespace(character):
            output_text += character
        else:
            output_text += decrypt_char(character)

    return output_text

print(decrypt('../1-pip-io-modules/01_io/texts/encoded_zen_lines.txt'))
