import turtle

def draw_square():
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.forward(75)

def draw_triangle():
    for _ in range(3):
        turtle.forward(50)
        turtle.left(120)
    turtle.forward(75)

def main():
    turtle.speed(1)
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(-250, 0)
    turtle.pendown()

    for _ in range(3):
        draw_square()
        draw_triangle()

    delay = input("Press enter to finish.")
    turtle.done()

if __name__ == "__main__":
    main()
