def draw_triangle(lines):
    BLACK_CHAR = '*'
    WHITE_CHAR = ' '
    output = ''
    for dots in range(1, lines + 1):
        position = lines - dots
        stars = dots * 2 - 1
        output += (WHITE_CHAR * position) + (BLACK_CHAR * stars) + '\n'
    return output

print(draw_triangle(8))
