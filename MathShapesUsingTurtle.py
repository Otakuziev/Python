import turtle as t
import random

tim = t.Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def draw_shape(side_number):
    angle = int(360 / side_number)
    for i in range(side_number):
        t.forward(100)
        t.right(angle)
for i in range(3, 8):
    t.color(random.choice(colors))
    draw_shape(i)


