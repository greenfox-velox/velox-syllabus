def count_letters(input_str):
    output = {}
    for char in input_str:
        if not char in output:
            output[char] = 0
        output[char] += 1
    return output
