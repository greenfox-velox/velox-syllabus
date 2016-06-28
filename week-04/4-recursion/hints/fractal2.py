from tkinter import *
import random
import math

root = Tk()
canvas = Canvas(root, width=800, height=700, bg='#1FCECB')
canvas.pack()

S3 = 3 ** .5

def square(x, y, s):
    canvas.create_rectangle(x, y, x+s, y+s, fill='yellow')
def circle(x, y, s, f='#A73E5C'):
    canvas.create_oval(x, y, x+s, y+s, fill=f, outline=f)
def triangle(x, y, s, f='lime green', o='black'):
    chance = random.random()
    randdiff = 300
    if chance > .9:
        x += random.randrange(-randdiff, randdiff)
        y += random.randrange(-randdiff, randdiff)
    a = [x, y]
    b = [x+s, y]
    c = [x+s/2, y+s*3**0.5/2]
    # if  .95 < chance < .98:
    #     c[0] += random.randrange(-randdiff, randdiff)
    #     c[1] += random.randrange(-randdiff, randdiff)
    # chance = random.random()
    #     a[0] += random.randrange(-randdiff, randdiff)
    #     a[1] += random.randrange(-randdiff, randdiff)
    canvas.create_polygon(a[0], a[1], b[0], b[1], c[0], c[1], fill=f)

def recsquare(x, y, s):
    if s <= SIZE_LIMIT:
        square(x, y, s)
    else:
        square(x, y, s)
        s /= 3
        recsquare(x+s, y, s)
        recsquare(x, y+s, s)
        recsquare(x+2*s, y+s, s)
        recsquare(x+s, y+2*s, s)

# recsquare(10, 10, 580)
colors = ['#5C2849', '#A73E5C', '#EC4863', '#FFDA66', '#1FCECB']
# colors = ['#334D5C', '#45B29D', '#EFC94C', '#E27A3F', '#DF5A49']
# colors = ['#FFFDD4', '#FFFF9D', '#BEEB9F', '#79BD8F', '#00A388']
SIZE_LIMIT = 20
DELAY = 500
def rectriangle(x, y, s):
    th = s*S3/4
    cr = S3*s/12
    stepest = int(math.log2(s))+2
    triangle(x, y, s, colors[stepest%len(colors)])
    circle(x+s/2-cr, y+th-cr*2, cr*2, colors[(stepest+1)%len(colors)])
    if s >= SIZE_LIMIT:
        s /= 2
        root.after(DELAY, rectriangle, x, y, s)
        root.after(DELAY+100, rectriangle, x+s, y, s)
        root.after(DELAY+200, rectriangle, x+s/2, y+th, s)
        root.after(DELAY+300, rectriangle, x+3/4*s, y+S3/4*s, s/2)

root.after(5000, rectriangle(20, 20, 760))

root.mainloop()
