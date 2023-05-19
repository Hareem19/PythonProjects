import turtle
wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.pencolor("white")
def curve():
    for i in range(200):
       t.rt(1)
       t.fd(1)
def heart():
    t.fillcolor("red")
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.fd(112)
    t.end.fill()
heart()
t.ht()
def write(message, pos):
    x,y = pos
    t.penup()
    t.goto(x,y)
    t.color()
    style = ["Stencil Std",18,"italic"]
t.write(message, fony=style)
write("i", (-42, 95))
write("l", (-42, 95))
write("o", (-42, 95))
write("v", (-42, 95))
write("e", (-42, 95))
write("V", (-30, 95))
wn.mainloop()