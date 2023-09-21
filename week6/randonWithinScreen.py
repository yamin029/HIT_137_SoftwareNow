import turtle  # Import the turtle module
import random  # Import the random module

def main():
    # Create a turtle named 't'
    t = turtle.Turtle()
    t.shape("turtle")  # Set the turtle shape to "turtle"
    t.color("red")  # Set the turtle color to "red"
    t.pensize(5)  # Set the pen size to 5
    t.speed(10)  # Set the drawing speed to 10

    # Create a turtle screen
    wn = turtle.Screen()
    wn.bgcolor("blue")  # Set the background color of the screen to "blue"

    def isInScreen(wn, t):
        # Calculate the boundaries of the screen
        xmin = -wn.window_width() / 2
        xmax = wn.window_width() / 2
        ymin = -wn.window_height() / 2
        ymax = wn.window_height() / 2
        x = t.xcor()  # Get the turtle's x-coordinate
        y = t.ycor()  # Get the turtle's y-coordinate

        # Check if the turtle is within the screen boundaries
        if x < xmin or x > xmax:
            return False
        if y < ymin or y > ymax:
            return False
        return True

    # Move the turtle while it's within the screen boundaries
    while isInScreen(wn, t):
        t.forward(50)  # Move the turtle forward by 50 units
        coin = random.randint(0, 2)  # Generate a random number (0, 1, or 2)
        if coin == 0:
            t.left(90)  # Turn the turtle left by 90 degrees
        else:
            t.right(90)  # Turn the turtle right by 90 degrees
    turtle.goto(0,0)
    # tuple.
    turtle.mainloop()  # Keep the turtle graphics window open

if __name__ == "__main__":
    main()  # Call the main function when the script is executed directly
