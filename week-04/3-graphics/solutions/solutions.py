from tkinter import *

root = Tk()

canvas_size = 400
canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()

# size = canvas_size // 8
# for i in range(8):
#     for j in range(8):
#         x = i * size
#         y = j * size
#         color = 'white'
#         if (i+j) % 2 == 0:
#             color = 'black'
#         canvas.create_rectangle(x, y, x+size, y+size, fill=color)

# for n in range(16):
#     i = n % 4
#     j = n // 4
#     ox = 40 * i
#     oy = 40 * j
#     canvas.create_rectangle(0 + ox, 0 + oy, 20 + ox, 20 + oy, fill='#000000')
#     canvas.create_rectangle(20 + ox, 20 + oy, 40 + ox, 40 + oy, fill='#000000')

half = canvas_size // 2
for i in range(0, half+1, 2):
    canvas.create_line(i, half, half, half-i, fill="lime green")
    canvas.create_line(canvas_size-i, half, half, half-i, fill="lime green")
    canvas.create_line(i, half, half, half+i, fill="lime green")
    canvas.create_line(canvas_size-i, half, half, half+i, fill="lime green")

root.mainloop()
