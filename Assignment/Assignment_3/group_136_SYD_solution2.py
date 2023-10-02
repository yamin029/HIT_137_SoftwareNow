import tkinter as tk
from tkinter import messagebox
import enchant

# Define the Task class to represent individual tasks in the to-do list
class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

# Define the ToDoListApp class, which represents the main application
class ToDoListApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("To-Do List App")

        # Create GUI elements (labels, entry fields, buttons)
        self.title_label = tk.Label(root, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack()

        # Initialize the list to store tasks and load existing tasks
        self.tasks = []
        self.load_tasks()

        # Create buttons for various actions
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack()

        # Create a frame for checkboxes below the task list
        self.checkbox_frame = tk.Frame(root)
        self.checkbox_frame.pack()

        # Update the task list in the GUI
        self.update_task_listbox()

        # Create an English dictionary for spelling check
        self.dictionary = enchant.Dict("en_US")

    # Method to check if the spelling is correct, skipping if the word starts with a capital letter
    def is_spelling_correct(self, text):
        if text[0].isupper():
            return True  # Skip spelling check for words starting with a capital letter
        else:
            return self.dictionary.check(text)

    # Method to add a new task to the list
    def add_task(self):
        # Get title and description from the user's input
        title = self.title_entry.get()
        description = self.description_entry.get()

        # Check if the title is empty
        if title:
            # Check spelling before adding the task
            if self.is_spelling_correct(title) and self.is_spelling_correct(description):
                # Create a new task and add it to the list
                task = Task(title, description)
                self.tasks.append(task)
                # Update the task list in the GUI and clear entry fields
                self.update_task_listbox()
                self.clear_entry_fields()
            else:
                messagebox.showwarning("Warning", "Spelling check failed. Please correct your input.")
        else:
            # Display a warning if the title is empty
            messagebox.showwarning("Warning", "Title cannot be empty!")

    # Method to edit an existing task
    def edit_task(self):
        # Get the index of the selected task in the listbox
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            # Get the new title and description from the user's input
            new_title = self.title_entry.get()
            new_description = self.description_entry.get()
            # Check if the new title is empty
            if new_title:
                # Check spelling before updating the task
                if self.is_spelling_correct(new_title) and self.is_spelling_correct(new_description):
                    # Update the selected task's title and description
                    self.tasks[selected_task_index].title = new_title
                    self.tasks[selected_task_index].description = new_description
                    # Update the task list in the GUI and clear entry fields
                    self.update_task_listbox()
                    self.clear_entry_fields()
                else:
                    messagebox.showwarning("Warning", "Spelling check failed. Please correct your input.")
            else:
                # Display a warning if the new title is empty
                messagebox.showwarning("Warning", "Title cannot be empty!")

    # Method to remove an existing task
    def remove_task(self):
        # Get the index of the selected task in the listbox
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            # Delete the selected task from the list
            del self.tasks[selected_task_index]
            # Update the task list in the GUI and clear entry fields
            self.update_task_listbox()
            self.clear_entry_fields()

    # Method to mark a task as completed
    def complete_task(self):
        # Get the index of the selected task in the listbox
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            # Mark the selected task as completed
            self.tasks[selected_task_index].completed = True
            # Update the task list in the GUI
            self.update_task_listbox()

    # Method to update the task list in the GUI
    def update_task_listbox(self):
        # Clear the task listbox and populate it with task titles
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Incomplete"
            self.task_listbox.insert(tk.END, f"{i+1}. {task.title} ({status})")

    # Method to clear the title and description entry fields
    def clear_entry_fields(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    # Method to save tasks to a text file
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.completed}\n")

    # Method to load tasks from a text file
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    title, description, completed = line.strip().split(',')
                    completed = bool(completed == 'True')
                    task = Task(title, description, completed)
                    self.tasks.append(task)
            # Update the task list in the GUI
            self.update_task_listbox()
        except FileNotFoundError:
            # If the file doesn't exist, ignore the error
            pass

# Main entry point of the program
if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    # Create an instance of the ToDoListApp class
    app = ToDoListApp(root)
    # Start the main event loop
    root.mainloop()
