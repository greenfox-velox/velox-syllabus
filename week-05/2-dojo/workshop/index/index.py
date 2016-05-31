def index(input_list, value):
    if not value in input_list: 
        return -1
    for i in range(len(input_list)):
        if input_list[i] == value:
            return i
