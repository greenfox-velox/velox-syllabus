def reverse_list(input_list):
    output_list = []
    i = len(input_list) - 1
    while i >= 0:
        output_list.append(input_list[i])
        i -= 1
    return output_list


