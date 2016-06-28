def is_palindrome(string):
    return string == string[::-1]

def palindromes(string):
    found_palindromes = []

    for frame_size in range(3,len(string)):
        for offset in range(len(string)-frame_size):
            current_substring = string[offset:offset+frame_size]
            if is_palindrome(current_substring):
                found_palindromes.append(current_substring)

    return found_palindromes

print(palindromes('dog goat dad duck doodle never'))

s = 'abcde'
print(s[-2:0:-1]) # even
