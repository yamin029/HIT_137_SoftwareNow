#####
# Group Number: 136
# STUDENT NAME: Yamin Hossain
# STUDENT NUMBER: S371068
# STUDENT NAME: SALMA FARIHA EERA
# STUDENT NUMBER: S371692
# STUDENT NAME: IFROIM DEWAN
# STUDENT NUMBER: 
####
# Import necessary libraries
import turtle  # Turtle graphics library for creating the clock
import time    # Time library for tracking and updating time
import math    # Math library for mathematical calculations

# Create a function to initialize the clock's appearance
def initialize_clock():
    # Create a turtle screen for drawing the clock
    window = turtle.Screen()
    window.title("Analog Wall Clock")  # Set the window title
    window.bgcolor("white")            # Set background color
    window.setup(width=600, height=600)  # Set the window dimensions
    window.tracer(0)  # Disable automatic screen updates

    # Create the clock face
    clock_face = turtle.Turtle()
    clock_face.speed(0)
    clock_face.color("black")
    clock_face.penup()
    clock_face.goto(0, -170)  # Position the clock face
    clock_face.pendown()
    clock_face.circle(190)    # Draw the clock circle
    clock_face.hideturtle()

    # Create a Turtle for displaying the time
    time_display = turtle.Turtle()
    time_display.speed(0)
    time_display.color("black")
    time_display.penup()
    time_display.hideturtle()
    time_display.goto(0, 260)
    time_display.write("", align="center", font=("Arial", 20, "normal"))

    # Create hour numbers and circles at appropriate positions
    clock_radius = 150

    for hour in range(1, 13):
        angle = math.radians(360 - (hour % 12) * 30)
        x = -clock_radius * math.sin(angle)
        y = clock_radius * math.cos(angle)

        # Create a circle below the hour number
        circle = turtle.Turtle()
        circle.speed(0)
        circle.penup()
        circle.goto(x, y + 20)  # Adjust the y-coordinate to position the circle
        if hour in [3, 6, 9, 12]:
            circle.color("red")  # Change the color of the circle for 12, 3, 6, 9
        else:
            circle.color("blue")  # Change the color of the circle for other hours
        circle.begin_fill()
        circle.circle(7)  # Adjust the radius as needed
        circle.end_fill()
        circle.hideturtle()

        # Create the hour number
        number = turtle.Turtle()
        number.speed(0)
        number.color("black")
        number.penup()
        number.goto(x, y)
        number.write(str(hour), align="center", font=("Arial", 12, "normal"))
        number.hideturtle()

        # Create and position the logo at the center of the clock
        text = "CDU"
        center_text = turtle.Turtle()
        center_text.speed(0)
        center_text.color("red")
        center_text.penup()
        center_text.goto(0, +110)
        center_text.write(text, align="center", font=("Arial", 12, "normal"))
        center_text.hideturtle()

    return window, clock_face, time_display

# Create a function to create a clock hand with an initial angle
def create_clock_hand(color, stretch_wid, stretch_len, initial_angle):
    clock_hand = turtle.Turtle()
    clock_hand.speed(0)
    clock_hand.shape("arrow")
    clock_hand.color(color)
    clock_hand.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len)
    clock_hand.penup()
    clock_hand.goto(0, 0)
    clock_hand.setheading(initial_angle)  # Set the initial angle
    return clock_hand

# Create a function to update the clock hands
def update_clock_hands(window, hour_hand, minute_hand, second_hand, time_display):
    current_time = time.localtime()
    second = current_time.tm_sec
    minute = current_time.tm_min
    hour = current_time.tm_hour % 12  # Convert to 12-hour format

    # Calculate angles for the hands
    second_angle = 97 - (second / 60) * 360
    minute_angle = 97 - ((minute + second / 60) / 60) * 360
    hour_angle = 97 - ((hour + minute / 60) / 12) * 360

    # Rotate the hands
    second_hand.setheading(second_angle)
    minute_hand.setheading(minute_angle)
    hour_hand.setheading(hour_angle)

    window.update()

    current_time_str = time.strftime("%I:%M:%S %p", current_time)
    time_display.clear()
    # time_display.write(current_time_str, align="center", font=("Arial", 20, "normal"))

# Main function to run the clock
def main():
    window, clock_face, time_display = initialize_clock()

    # Create clock hands with initial angles
    second_hand = create_clock_hand("black", 0.04, 12.5, 90)
    minute_hand = create_clock_hand("red", 0.1, 9, 90)
    hour_hand = create_clock_hand("green", 0.3, 7, 90)

    while True:
        update_clock_hands(window, hour_hand, minute_hand, second_hand, time_display)
        time.sleep(1)

    window.exitonclick()

if __name__ == "__main__":
    main()
