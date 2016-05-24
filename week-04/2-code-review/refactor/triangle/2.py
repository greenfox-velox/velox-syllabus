def draw_triangle(lines):
    output = ''
    position = lines - 1
    stars = 1
    for dots in range(1, lines + 1):
        output += (" " * position) + ("*" * stars) + '\n'
        stars += 2
        position -= 1
    return output

print(draw_triangle(8))
