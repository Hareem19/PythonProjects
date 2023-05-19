import turtle
from pygame import mixer

mixer.init()
mixer.music.load("hbd.mp3")
mixer.music.play()

wn = turtle.Screen()
wn.bgcolor("crimson")
t = turtle.Turtle()
t.pencolor("White")

def curve():
    for i in range(200):
       t.right(1)
       t.forward(1)

def heart():
    t.fillcolor("cyan2")
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()
t.hideturtle()
def write(message, pos):
    x,y = pos
    t.penup()
    t.goto(x,y)
    t.color("Black")
    style = ("Stencil Std", 18, "italic")
    t.write(message, font=style)

write("H", (-13*4, 95))
write("a", (-12.5*3, 95))
write("p", (-13*2, 95))
write("p", (-13, 95))
write("y", (0, 95))
write("B", (0, 71))
write("i", (15, 71))
write("r", (11*2, 71))
write("t", (11*3, 71))
write("h", (11*4, 71))
write("D", (-13*3, 57))
write("a", (-13*2, 57))
write("y", (-13*1, 57))
wn.mainloop()
