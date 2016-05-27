def draw_triangle(lines):
    BLACK_CHAR = '*'
    WHITE_CHAR = ' '
    output = ''
    for n in range(lines):
        position = lines - n - 1
        stars = n * 2 + 1
        output += (WHITE_CHAR * position) + (BLACK_CHAR * stars) + '\n'
    return output

print(draw_triangle(8))
