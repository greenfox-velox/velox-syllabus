def draw_triangle(lines):
    output = ''
    stars = 1
    for dots in range(1, lines + 1):
        position = lines - dots
        output += (" " * position) + ("*" * stars) + '\n'
        stars += 2
    return output

print(draw_triangle(8))
