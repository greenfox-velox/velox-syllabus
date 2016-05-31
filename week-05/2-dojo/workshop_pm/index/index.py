def index(input_list, value):
    if value in input_list:
        for i in range(len(input_list)):
            if input_list[i] == value:
                return i
    return -1
