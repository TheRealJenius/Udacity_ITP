import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

# Write whatever code you want here!
mikey = turtle.Turtle()
mikey.width(3)
mikey.speed(6) #0 being the fastest
for colours in rainbow:
    mikey.color(colours)
    mikey.penup()
    mikey.back(100)
    mikey.pendown()
    
    mikey.forward(100)
    mikey.right(60)
    mikey.penup()
    mikey.back(100)
    mikey.pendown()
    mikey.right(60)
    mikey.forward(100)
    mikey.penup()
    mikey.left(120)
    mikey.forward(100)
    mikey.right(60)
    mikey.pendown()

