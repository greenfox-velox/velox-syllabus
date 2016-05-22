in_file = open("texts/zen_of_python.txt", "r")
out_file = open("texts/encoded_zen_lines.txt", "w")

for line in in_file:
    raw_line = line.rstrip()
    words = raw_line.split()

    encoded_words = []
    for word in words:
        encoded_word = ""
        for char in word:
            encoded_word += chr(ord(char) + 1)

        encoded_words.append(encoded_word)

    encoded_line = " ".join(encoded_words)

    out_file.write(encoded_line + "\n")

in_file.close()
out_file.close()

print('ready')
