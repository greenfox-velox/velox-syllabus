from tkinter import *
from ball import Ball

master = Tk()

canvas = Canvas(master, width=400, height=400)
canvas.pack()

ball = Ball((100, 150), (0, 2), 10)

while True:
    ball.move()
    bbox = ball.get_bbox()
    canvas.create_rectangle(0, 0, 400, 400, fill='#ffffff')
    canvas.create_oval(bbox, fill='#000000')
    canvas.after(1000 // 60)
    canvas.update()


mainloop()
