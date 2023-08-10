import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Create a custom dialog for text input
class TextInputDialog(tk.Toplevel):
    def __init__(self, title, prompt):
        super().__init__()
        self.title(title)
        self.prompt = prompt
        self.result = None

        self.label = tk.Label(self, text=prompt)
        self.label.pack(padx=10, pady=5)

        self.entry = tk.Entry(self)
        self.entry.pack(padx=10, pady=5)

        self.ok_button = tk.Button(self, text="OK", command=self.on_ok)
        self.ok_button.pack(pady=5)

    def on_ok(self):
        self.result = self.entry.get()
        self.destroy()

def get_text_input(title, prompt):
    dialog = TextInputDialog(title, prompt)
    dialog.wait_window()
    return dialog.result

def create_file():
    file_path = filedialog.asksaveasfilename(title="Create File", defaultextension=".txt")
    if not file_path:
        return

    if os.path.exists(file_path):
        messagebox.showinfo("File Already Exists", f"The file '{file_path}' already exists.")
    else:
        try:
            with open(file_path, 'w') as file:
                file.write('')
            messagebox.showinfo("File Created", f"The file '{file_path}' has been created successfully.")
        except Exception as e:
            messagebox.showerror("Error Creating File", f"An error occurred while creating the file:\n{str(e)}")

def delete_file():
    file_path = filedialog.askopenfilename(title="Delete File")
    if not file_path:
        return

    if not os.path.exists(file_path):
        messagebox.showinfo("File Not Found", f"The file '{file_path}' does not exist.")
    else:
        try:
            os.remove(file_path)
            messagebox.showinfo("File Deleted", f"The file '{file_path}' has been deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error Deleting File", f"An error occurred while deleting the file:\n{str(e)}")

def read_file():
    file_path = filedialog.askopenfilename(title="Read File")
    if not file_path:
        return

    if not os.path.exists(file_path):
        messagebox.showinfo("File Not Found", f"The file '{file_path}' does not exist.")
    else:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            messagebox.showinfo("File Content", f"Content of file '{file_path}':\n{content}")
        except Exception as e:
            messagebox.showerror("Error Reading File", f"An error occurred while reading the file:\n{str(e)}")

def write_file():
    file_path = filedialog.askopenfilename(title="Write File")
    if not file_path:
        return

    content = get_text_input("Enter Content", "Enter the content to write:")
    if content is None:
        return

    try:
        with open(file_path, 'w') as file:
            file.write(content)
        messagebox.showinfo("Content Written", f"Content written to file '{file_path}' successfully.")
    except Exception as e:
        messagebox.showerror("Error Writing to File", f"An error occurred while writing to the file:\n{str(e)}")

def create_directory():
    def on_ok():
        nonlocal dir_name, parent_path
        dir_name = entry_name.get()
        parent_path = entry_path.get()
        root.destroy()

    root = tk.Toplevel()
    root.title("Create Directory")

    dir_name = ""
    parent_path = ""

    label_name = tk.Label(root, text="Enter the name of the directory:")
    label_name.pack(padx=10, pady=5)

    entry_name = tk.Entry(root)
    entry_name.pack(padx=10, pady=5)

    label_path = tk.Label(root, text="Select Parent Directory:")
    label_path.pack(padx=10, pady=5)

    entry_path = tk.Entry(root)
    entry_path.pack(padx=10, pady=5)

    ok_button = tk.Button(root, text="OK", command=on_ok)
    ok_button.pack(pady=5)

    root.wait_window()

    if not dir_name or not parent_path:
        return

    dir_path = os.path.join(parent_path, dir_name)

    if os.path.exists(dir_path):
        messagebox.showinfo("Directory Already Exists", f"The directory '{dir_path}' already exists.")
    else:
        try:
            os.makedirs(dir_path)
            messagebox.showinfo("Directory Created", f"Directory '{dir_path}' has been created successfully.")
        except Exception as e:
            messagebox.showerror("Error Creating Directory", f"An error occurred while creating the directory:\n{str(e)}")


def delete_directory():
    dir_path = filedialog.askdirectory(title="Delete Directory")
    if not dir_path:
        return

    if not os.path.exists(dir_path):
        messagebox.showinfo("Directory Not Found", f"The directory '{dir_path}' does not exist.")
    else:
        try:
            os.rmdir(dir_path)
            messagebox.showinfo("Directory Deleted", f"Directory '{dir_path}' has been deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error Deleting Directory", f"An error occurred while deleting the directory:\n{str(e)}")

# Create the main application window
root = tk.Tk()
root.title("Sushant's File System ")

# Set window size and background color
root.geometry("600x400")
root.configure(bg="black")

button_bg = "white"
button_text_color = "green"

# Create buttons for each operation with red background and white text
btn_create_file = tk.Button(root, text="Create File", command=create_file, bg=button_bg, fg=button_text_color)
btn_delete_file = tk.Button(root, text="Delete File", command=delete_file, bg=button_bg, fg=button_text_color)
btn_read_file = tk.Button(root, text="Read File", command=read_file, bg=button_bg, fg=button_text_color)
btn_write_file = tk.Button(root, text="Write File", command=write_file, bg=button_bg, fg=button_text_color)
btn_create_directory = tk.Button(root, text="Create Directory", command=create_directory, bg=button_bg, fg=button_text_color)
btn_delete_directory = tk.Button(root, text="Delete Directory", command=delete_directory, bg=button_bg, fg=button_text_color)
btn_exit = tk.Button(root, text="Exit", command=root.quit, bg=button_bg, fg=button_text_color)

# Pack the buttons in the window
btn_create_file.pack(pady=5)
btn_delete_file.pack(pady=5)
btn_read_file.pack(pady=5)
btn_write_file.pack(pady=5)
btn_create_directory.pack(pady=5)
btn_delete_directory.pack(pady=5)
btn_exit.pack(pady=10)

# Start the main event loop
root.mainloop()
