import turtle
dongu = 0

turtle.penup()
turtle.goto(100,250)
turtle.pendown()
while dongu != 3:
    dongu = dongu + 1
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
turtle.forward(200)
turtle.exitonclick()