from turtle import *
color ('green','blue')
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()