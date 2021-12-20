import turtle
turtle.bgcolor("black")
painter = turtle.Turtle()
painter.speed(0)
painter.penup()
painter.left(90)
painter.goto(0,0)
painter.forward(100)
painter.left(180)
painter.pendown()
j=0
while(j<=5):
    
    painter.pencolor("red")
    for i in range(150):
        painter.forward(100)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark violet")
    for i in range(150):
        painter.forward(104)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("dark red")
    for i in range(150):
        painter.forward(106)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark orange")
    for i in range(150):
        painter.forward(104)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark grey")
    for i in range(150):
        painter.forward(100)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("red")
    for i in range(150):
        painter.forward(100)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark violet")
    for i in range(150):
        painter.forward(104)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()
 
    painter.pencolor("dark red")
    for i in range(150):
        painter.forward(106)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark orange")
    for i in range(150):
        painter.forward(104)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark grey")
    for i in range(150):
        painter.forward(100)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

j=j+1
turtle.done()
turtle.quit()
j=j+1
turtle.done()
turtle.quit()
