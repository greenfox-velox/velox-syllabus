from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()

def square(x, y, s):
    canvas.create_rectangle(x, y, x+s, y+s, fill='yellow')

SIZE_LIMIT = 3
def recsquare(x, y, s):
    if (s <= SIZE_LIMIT):
        square(x, y, s)
    else:
        square(x, y, s)
        s /= 3
        recsquare(x+s, y, s)
        recsquare(x, y+s, s)
        recsquare(x+2*s, y+s, s)
        recsquare(x+s, y+2*s, s)

recsquare(10, 10, 580)

root.mainloop()
