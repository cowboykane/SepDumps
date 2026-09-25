import tkinter as tk
from tkinter import ttk

root = tk.Tk(className="Something in the waaay")
root.geometry("550x500")

label = tk.Label(root, text="This is a damn label like girl...idk")
label.pack()

label2 = tk.Label(root, text="Heres another one", fg="blue")
label2.pack()

button = tk.Button(root, text="Beater")
button.pack()

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu  = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")


text_widget = tk.Text(root)
text_widget.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

root.mainloop()