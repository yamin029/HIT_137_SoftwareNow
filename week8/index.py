# from tkinter import *

# root = Tk()
# label1 = Label(root, text="This is my fist Python GUI based app \n Developed by Yamin Hossain")
# label1.pack()
# root.mainloop()

# from tkinter import *

# root = Tk()

# # Frame is a rectangular area that can contain other widgets
# topFrame = Frame(root)
# topFrame.pack()

# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# button1 = Button(topFrame, text="Button 1", fg="red")
# button2 = Button(topFrame, text="Button 2", fg="blue")
# button3 = Button(topFrame, text="Button 3", fg="green")
# button4 = Button(bottomFrame, text="Button 4", fg="purple")

# # These buttons will be on top
# button1.pack(side=LEFT)  # place as far left as possible
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)

# # Button 4 is on the bottom
# button4.pack(side=BOTTOM)

# root.mainloop()

# from tkinter import *

# root = Tk()

# one = Label(root, text="One", bg="red", fg="white")
# one.pack()

# two = Label(root, text="Two", bg="green", fg="black")
# two.pack(fill=X)  # fill=X - makes the widget as wide as the parent

# three = Label(root, text="Three", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)

# root.mainloop()

# from tkinter import *

# # Create the main application window
# root = Tk()

# # Create labels for Name and Password fields
# label_1 = Label(root, text="Name")
# label_2 = Label(root, text="Password")

# # Create entry widgets for user input
# entry_1 = Entry(root)
# entry_2 = Entry(root)

# # Widgets are centered by default, but you can change their alignment with the 'sticky' option
# label_1.grid(row=0, sticky=E)  # Place label_1 in row 0, right-aligned (East)
# label_2.grid(row=1, sticky=E)  # Place label_2 in row 1, right-aligned (East)
# entry_1.grid(row=0, column=1)  # Place entry_1 in row 0, column 1
# entry_2.grid(row=1, column=1)  # Place entry_2 in row 1, column 1

# # Widgets can take up more than one cell using 'columnspan' and 'rowspan'
# c = Checkbutton(root, text="Keep me logged in")
# c.grid(columnspan=2)  # Span the widget across 2 columns

# # Start the main event loop
# root.mainloop()

# from tkinter import *

# # Create the main application window
# root = Tk()

# # Define a function to print a message when the button is clicked
# def printName(event):
#     print("Programming is fun")

# # Create a button widget
# button_1 = Button(root, text="Print Message")

# # Bind the printName function to the "<Button-1>" event (left mouse button click)
# button_1.bind("<Button-1>", printName)

# # Place the button widget in the window
# button_1.pack()

# # Start the main event loop
# root.mainloop()

# from tkinter import *

# # Create the main application window
# root = Tk()

# # Define functions to handle left, middle, and right mouse button clicks
# def leftClick(event):
#     print("Left")

# def middleClick(event):
#     print("Middle")

# def rightClick(event):
#     print("Right")

# # Create a frame widget with a specific width and height
# frame = Frame(root, width=300, height=200)

# # Bind the functions to the corresponding mouse button events
# frame.bind("<Button-1>", leftClick)  # Left mouse button click
# frame.bind("<Button-2>", middleClick)  # Middle mouse button click
# frame.bind("<Button-3>", rightClick)  # Right mouse button click

# # Place the frame widget in the window
# frame.pack()

# # Start the main event loop
# root.mainloop()

# from tkinter import *

# class BuckysButtons:
#     def __init__(self, master):
#         # Create a frame and pack it into the master widget
#         frame = Frame(master)
#         frame.pack()

#         # Create a "Print Message" button with a command to call printMessage method
#         self.printButton = Button(frame, text="Print Message", command=self.printMessage)
#         self.printButton.pack(side=LEFT)

#         # Create a "Quit" button with a command to quit the frame
#         self.quitButton = Button(frame, text="Quit", command=frame.quit)
#         self.quitButton.pack(side=LEFT)

#     def printMessage(self):
#         print("Wow, this actually worked!")

# # Create the main application window
# root = Tk()

# # Create an instance of the BuckysButtons class with the main window as the master
# b = BuckysButtons(root)

# # Start the main event loop
# root.mainloop()


# from tkinter import *

# # Function to do nothing (placeholder)
# def doNothing():
#     print("Do nothing...")

# # Create the main application window
# root = Tk()

# # Create a menu bar
# menu = Menu(root)
# root.config(menu=menu)

# # Create a "File" submenu
# subMenu = Menu(menu)
# menu.add_cascade(label="File", menu=subMenu)

# # Add commands and a separator to the "File" submenu
# subMenu.add_command(label="New Project", command=doNothing)
# subMenu.add_command(label="New...", command=doNothing)
# subMenu.add_separator()
# subMenu.add_command(label="Exit", command=root.quit)

# # Create an "Edit" submenu
# editMenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editMenu)

# # Add a command to the "Edit" submenu
# editMenu.add_command(label="Redo", command=doNothing)

# # Start the main event loop
# root.mainloop()

# from tkinter import *

# # Function to do nothing (placeholder)
# def doNothing():
#     print("Do nothing")

# # Create the main application window
# root = Tk()

# # ***** Main Menu *****
# menu = Menu(root)
# root.config(menu=menu)

# # Create a "File" submenu
# subMenu = Menu(menu)
# menu.add_cascade(label="File", menu=subMenu)
# subMenu.add_command(label="New Project", command=doNothing)
# subMenu.add_command(label="New...", command=doNothing)
# subMenu.add_separator()
# subMenu.add_command(label="Exit", command=doNothing)

# # Create an "Edit" submenu
# editMenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="Redo", command=doNothing)

# # ***** The Toolbar *****
# toolbar = Frame(root, bg="blue")

# # Create "Insert Image" button in the toolbar
# insertButt = Button(toolbar, text="Insert Image", command=doNothing)
# insertButt.pack(side=LEFT, padx=2, pady=2)

# # Create "Print" button in the toolbar
# printButt = Button(toolbar, text="Print", command=doNothing)
# printButt.pack(side=LEFT, padx=2, pady=2)

# # Pack the toolbar at the top, filling the horizontal space
# toolbar.pack(side=TOP, fill=X)

# # Start the main event loop
# root.mainloop()

from tkinter import *

# Function to do nothing (placeholder)
def doNothing():
    print("Do nothing")

# Create the main application window
root = Tk()

# ***** Main Menu *****
menu = Menu(root)
root.config(menu=menu)

# Create a "File" submenu
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

# Create an "Edit" submenu
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# ***** The Toolbar *****
toolbar = Frame(root, bg="blue")

# Create "Insert Image" button in the toolbar
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)

# Create "Print" button in the toolbar
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

# Pack the toolbar at the top, filling the horizontal space
toolbar.pack(side=TOP, fill=X)

# ***** Status Bar *****
status = Label(root, text="Preparing to do nothing...", bd=10, relief=GROOVE, anchor=W)
status.pack(side=BOTTOM, fill=X)

# Start the main event loop
root.mainloop()
