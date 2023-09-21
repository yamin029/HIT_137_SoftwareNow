import turtle
import random

def main():
    loadWindow = turtle.Screen()
    loadWindow.bgcolor("#AAAAFF")

    turtle1 = turtle.Pen()
    turtle1.shape("turtle")
    turtle2 = turtle.Pen()
    turtle2.shape("circle")
    turtle3 = turtle.Pen()
    turtle3.shape("square")
    turtle4 = turtle.Pen()
    turtle4.shape("triangle")

    turtle1.left(90)
    turtle2.forward(-50)
    turtle2.left(90)
    turtle3.forward(50)
    turtle3.left(90)
    turtle4.forward(100)
    turtle4.left(90)

    for x in range(100):
        t1 = random.randint(-5, 30)
        t2 = random.randint(-5, 30)
        t3 = random.randint(-5, 30)
        t4 = random.randint(-5, 30)
        
        turtle1.forward(t1)
        turtle2.forward(t2)
        turtle3.forward(t3)
        turtle4.forward(t4)

    turtle.exitonclick()

if __name__ == "__main__":
    main()
