def draw_triangle(lines):
    output = ''
    for dots in range(1, lines + 1):
        position = lines - dots
        stars = dots * 2 - 1
        output += (' ' * position) + ('*' * stars) + '\n'
    return output

print(draw_triangle(8))
