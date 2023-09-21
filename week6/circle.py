import turtle

def main():
    loadWindow = turtle.Screen()
    loadWindow.bgcolor("#AAAAFF")
    turtle.delay(10)

    turtle1 = turtle.Pen()
    turtle1.color("red")
    turtle2 = turtle.Pen()
    turtle2.color("green")
    turtle3 = turtle.Pen()
    turtle3.color("blue")
    turtle4 = turtle.Pen()
    turtle4.color("yellow")

    for x in range(100):
        turtle1.circle(100)
        turtle1.left(90)
        turtle2.circle(100)
        turtle2.right(90)
        turtle3.forward(-100)
        turtle3.left(90)
        turtle4.forward(-100)
        turtle4.right(90)

    turtle.exitonclick()

if __name__ == "__main__":
    main()
