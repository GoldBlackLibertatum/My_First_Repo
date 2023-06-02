from turtle import *
#Sets Up The Title, Color of Turtle, Screen Size, and Screen Positioning on Screen Open
title("Dodecagon")
setup(width= 1000, height= 1000, startx= 0, starty= 0)
setworldcoordinates(-500,-500,500,500)
t1 = Turtle()
t1.color("orange", "grey")
t1.begin_fill()
for _ in range (12):
    t1.forward(100)
    t1.left(30)    
t1.end_fill()
done()
