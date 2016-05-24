def draw_triangle(lines):
    position = lines - 1
    stars = 1
    for dots in range(1, lines + 1):
        print ((" " * position) + ("*" * stars))
        stars += 2
        position -= 1
    return

print(draw_triangle(8))
