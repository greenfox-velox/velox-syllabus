from tkinter import *

root = Tk()

canvas = Canvas(root, width='200', height='100')
canvas.pack()

teal_line = canvas.create_line(0, 0, 200, 50, fill='light sea green')
lime_box = canvas.create_rectangle(50, 50, 100, 90, fill='lime green')
olive_oval = canvas.create_oval(120, 10, 180, 90, fill='olive drab')

root.mainloop()
