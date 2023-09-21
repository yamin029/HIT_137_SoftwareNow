import tkinter as tk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

class ToDoListApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("To-Do List App")

        # Initialize the list to store tasks and load existing tasks
        self.tasks = []
        self.load_tasks()

        # Create GUI elements (labels, entry fields, buttons)
        self.title_label = tk.Label(root, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack()

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

    def add_task(self):
        # Get title and description from the user's input
        title = self.title_entry.get()
        description = self.description_entry.get()

        # Check if the title is empty
        if title:
            # Create a new task and add it to the list
            task = Task(title, description)
            self.tasks.append(task)
            # Update the task list in the GUI and clear entry fields
            self.update_task_listbox()
            self.clear_entry_fields()
        else:
            # Display a warning if the title is empty
            messagebox.showwarning("Warning", "Title cannot be empty!")

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
                # Update the selected task's title and description
                self.tasks[selected_task_index].title = new_title
                self.tasks[selected_task_index].description = new_description
                # Update the task list in the GUI and clear entry fields
                self.update_task_listbox()
                self.clear_entry_fields()
            else:
                # Display a warning if the new title is empty
                messagebox.showwarning("Warning", "Title cannot be empty!")

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

    def complete_task(self):
        # Get the index of the selected task in the listbox
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            # Mark the selected task as completed
            self.tasks[selected_task_index].completed = True
            # Update the task list in the GUI
            self.update_task_listbox()

    def update_task_listbox(self):
        # Clear the task listbox and populate it with task titles
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Incomplete"
            self.task_listbox.insert(tk.END, f"{i+1}. {task.title} ({status})")

        # # Clear the checkboxes frame and create checkboxes
        # for widget in self.checkbox_frame.winfo_children():
        #     widget.destroy()

        # for i, task in enumerate(self.tasks):
        #     status = "Completed" if task.completed else "Incomplete"
        #     task_checkbox = tk.Checkbutton(self.checkbox_frame, text=f"{i+1}. {task.title}", command=lambda i=i: self.toggle_complete(i))
        #     task_checkbox.select() if task.completed else task_checkbox.deselect()
        #     task_checkbox.pack(anchor="w")

    # def toggle_complete(self, index):
    #     # Toggle the completion status of the selected task
    #     self.tasks[index].completed = not self.tasks[index].completed
    #     # Update the task list in the GUI
    #     self.update_task_listbox()


    def clear_entry_fields(self):
        # Clear the title and description entry fields
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def save_tasks(self):
        # Save tasks to a text file
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.completed}\n")

    def load_tasks(self):
        try:
            # Load tasks from a text file
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

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
