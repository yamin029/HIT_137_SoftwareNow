from tkinter import *
import tkinter.messagebox

# Create the main application window
root = Tk()

# Show an information message box
tkinter.messagebox.showinfo('Window Title', 'Subject Code')

# Ask a question and store the answer
answer = tkinter.messagebox.askquestion('Question 1', 'Do you want to display your subject code')

# Check the answer and print a message if it's 'yes'
if answer == 'yes':
    print("HIT 137")

# Start the main event loop
root.mainloop()
