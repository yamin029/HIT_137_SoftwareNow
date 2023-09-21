import turtle

# Define constants with capital letters
SQUARE = 4
TRIANGLE = 3
PENTAGON = 5
HEXAGON = 6

def draw_shape(sides, color):
    turtle.color(color)
    for _ in range(sides):  # Use '_' since we don't use 'i' inside the loop
        turtle.forward(50)
        turtle.left(360 / sides)
    turtle.forward(75)

def main():
    # turtle.speed(2)
    turtle.shape("turtle")
    turtle.goto(-250, 0)

    # Draw shapes using constants
    draw_shape(SQUARE, "blue")
    draw_shape(TRIANGLE, "red")
    draw_shape(PENTAGON, "green")
    draw_shape(HEXAGON, "purple")

    turtle.goto(-250, 90)  # Move up
    draw_shape(SQUARE, "blue")
    draw_shape(TRIANGLE, "red")
    draw_shape(PENTAGON, "green")
    draw_shape(HEXAGON, "purple")

    delay = input("Press enter to finish.")

if __name__ == "__main__":
    main()
