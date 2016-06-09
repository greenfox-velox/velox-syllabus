from tkinter import *

def main():
  root = Tk()
  canvas = Canvas(root, width=400, height=400)
  canvas.pack()
  canvas.focus_set()
  box = Box(400, 400)
  blink(canvas, box)
  root.mainloop()

class Ball(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw(self, canvas):
    size = 40
    canvas.create_rectangle(self.x, self.y, self.x + size, self.y + size, fill="blue")

  def move(self, x, y):
    self.x += x
    self.y += y

class Box(object):
  def __init__(self, size_x, size_y):
    self.size_x = size_x
    self.size_y = size_y
    self.balls = [
      Ball(100, 100),
      Ball(20, 50),
      Ball(120, 180)
    ]

  def exec_and_draw(self, canvas):
    for ball in self.balls:
      ball.move(2, 0)
      ball.draw(canvas)


def blink(canvas, box):
  canvas.create_rectangle(0, 0, 400, 400, fill="white")
  box.exec_and_draw(canvas)
  canvas.after(33, blink, canvas, box)

main()
