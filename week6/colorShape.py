import turtle

def draw_shape(shape, color):
    turtle.color(color)
    turtle.pendown()
    if shape == "square":
        for _ in range(4):
            turtle.forward(50)
            turtle.left(90)
        turtle.forward(75)

    if shape == "triangle":
        for _ in range(3):
            turtle.forward(50)
            turtle.left(120)
        turtle.forward(75)

def main():
    turtle.speed(1)
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(-250, 0)

    draw_shape("square", "blue")
    draw_shape("triangle", "red")
    draw_shape("square", "green")
    draw_shape("triangle", "purple")

    delay = input("Press enter to finish.")

if __name__ == "__main__":
    main()
