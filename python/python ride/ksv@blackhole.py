import turtle 
import random 
turtle.speed(0)
Speedy = turtle.Turtle()

Speedy.speed(999)

Speedy.color("Black")
turtle.bgcolor('gold')

while True:
    Speedy.forward(180)
    Speedy.left(70)
    Speedy.forward(60)
    Speedy.right(random.randint(40,70))
    
    Speedy.penup()
    Speedy.setposition(0, 0)
    Speedy.pendown()
    
    Speedy.right(random.randint(2,10))
    
