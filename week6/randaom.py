import turtle
import random

def main():
    # Create a turtle named 't'
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("red")
    t.pensize(5)

    # Create a turtle screen
    wn = turtle.Screen()
    wn.bgcolor("blue")

    # Draw a sequence of lines
    for i in range(40):
        t.forward(50)

        # Randomly choose left or right turn
        coin = random.randint(0, 1)
        if coin == 0:
            t.left(90)
        else:
            t.right(90)

    # Keep the turtle graphics window open
    turtle.mainloop()

if __name__ == "__main__":
    main()
