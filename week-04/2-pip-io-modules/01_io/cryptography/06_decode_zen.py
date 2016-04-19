encoded_file = open("texts/encoded_zen_lines.txt", "r")

for line in encoded_file:
    raw_line = line.rstrip()
    words = raw_line.split()

    decoded_words = []
    for word in words:
        decoded_word = ""
        for char in word:
            decoded_word += chr(ord(char) - 1)
        decoded_words.append(decoded_word)

    decoded_line = " ".join(decoded_words)

    print(decoded_line)

encoded_file.close()
