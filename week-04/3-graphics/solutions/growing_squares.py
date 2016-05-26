from tkinter import *

root = Tk()

canvas = Canvas(root, width='400', height='400')
canvas.pack()

offset = 0
size = 10
while offset+size <= 300:
    canvas.create_rectangle(
        offset, offset,
        offset+size, offset+size,
        fill='yellow'
        )
    offset += size
    size += 10

root.mainloop()
