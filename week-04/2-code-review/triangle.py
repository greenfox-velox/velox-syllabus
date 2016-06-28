def draw_triangle(lines):
    WHITE = ' '
    BLACK = 'o'
    printable = ''
    for i in range(lines):
        position = lines - i - 1
        stars = 2 * i + 1
        printable += (WHITE * position) + (BLACK * stars)
        if i < lines - 1:
            printable += '\n'
    return printable

print(draw_triangle(8))
