
# Stupid notepad

# Bones:

"""
1. Need a basic ui framework to act as the notepad itself
2. Notepad needs to accept user input
3. User should be able to save the input into a txt or any type of file
4. User should be able to name open file

What do I need to know?

- File handling (good)
- The framwork for the gui: Tkinter

"""

import tkinter as tk
from tkinter import filedialog
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Window
root = tk.Tk(className="Wicked Notepad")
root.geometry("550x500")

# Menu
menu = tk.Menu(root)
root.config(menu=menu)

# -- Functions --

# Save feature 

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if file_path:
        content = text_box.get("1.0", tk.END)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
            
# New file feature

def new_file():
    file_path = filedialog.askopenfile
    text_box.delete("1.0", tk.END)
    
def open_file():
    file_path = filedialog.askopenfilename()


# The filemenu, options: new, open, save
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open...", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Edit menu, options: Undo, Cut, Copy
editmenu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")

# Scrollbar
v_scrollbar = tk.Scrollbar(root, orient="vertical")
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
h_scrollbar = tk.Scrollbar(root, orient="horizontal")
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Textbox
text_box = tk.Text(root, wrap="none",
                   xscrollcommand=h_scrollbar.set,
                   yscrollcommand=v_scrollbar.set,
                   font=("Consolas", 10))
text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

v_scrollbar.config(command=text_box.yview)
h_scrollbar.config(command=text_box.xview)


root.mainloop()