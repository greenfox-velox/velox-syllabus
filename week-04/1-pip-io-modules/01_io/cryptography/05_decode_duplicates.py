encoded_file = open("texts/duplicated_chars.txt", "r")

for line in encoded_file:
    raw_line = line.rstrip()
    words = raw_line.split()

    cleaned_words = []
    for word in words:
        cleaned_words.append(word[::2])

    print(" ".join(cleaned_words))

encoded_file.close()
