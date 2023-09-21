import turtle

# Function to draw a letter 'Y'
def draw_letter_Y():
    turtle.penup()           # Lift the pen (no drawing while moving)
    turtle.goto(-50, 0)      # Move to the starting position
    turtle.pendown()         # Lower the pen (start drawing)
    turtle.goto(0, 100)      # Draw the left stroke of 'Y'
    turtle.goto(50, 0)       # Draw the right stroke of 'Y'
    turtle.penup()           # Lift the pen
    turtle.goto(25, 50)      # Move to the next letter's starting position
    turtle.pendown()         # Lower the pen

# Function to draw a letter 'A'
def draw_letter_A():
    turtle.penup()
    turtle.goto(75, 100)
    turtle.pendown()
    turtle.goto(100, 0)
    turtle.goto(125, 100)
    turtle.penup()
    turtle.goto(87.5, 50)
    turtle.pendown()

# Function to draw a letter 'M'
def draw_letter_M():
    turtle.penup()
    turtle.goto(150, 0)
    turtle.pendown()
    turtle.goto(150, 100)
    turtle.goto(175, 50)
    turtle.goto(200, 100)
    turtle.goto(200, 0)

# Function to draw a letter 'I'
def draw_letter_I():
    turtle.penup()
    turtle.goto(225, 100)
    turtle.pendown()
    turtle.goto(250, 100)
    turtle.penup()
    turtle.goto(237.5, 50)
    turtle.pendown()

# Function to draw a letter 'N'
def draw_letter_N():
    turtle.penup()
    turtle.goto(275, 0)
    turtle.pendown()
    turtle.goto(275, 100)
    turtle.goto(300, 0)
    turtle.goto(300, 100)

def main():
    turtle.speed(1)          # Set the drawing speed to 1 (slowest)
    turtle.shape("turtle")   # Set the turtle shape to "turtle"

    name = "YAMIN"
    letter_spacing = 25

    for letter in name:
        if letter == "Y":
            draw_letter_Y()
        elif letter == "A":
            draw_letter_A()
        elif letter == "M":
            draw_letter_M()
        elif letter == "I":
            draw_letter_I()
        elif letter == "N":
            draw_letter_N()
        turtle.penup()
        turtle.forward(letter_spacing)  # Move forward to create spacing

    delay = input("Press enter to finish.")  # Wait for user input
    turtle.done()             # Close the Turtle graphics window

if __name__ == "__main__":
    main()
