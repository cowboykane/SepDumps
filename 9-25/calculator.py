
# Calculator!

# Bones:

"""
1. Use tkinter for the gui
2. Calculator needs a display that responds to the buttons
3. Calculator needs basic buttons and numbers
4. User needs to be able to input and perform actions on the on-screen calculator

-

Create display and buttons on tkinter, maybe a frame?

"""

import tkinter as tk

root = tk.Tk()
root.title("Calculator")
icon = tk.PhotoImage(file=r"D:\VSCODE\SepDumps\SepDumps\9-25\basic-arithmetic-quiz-icon-color.png")
root.iconphoto(True, icon)

root.geometry("320x500")

frame = tk.Frame(root)


# Labels: 
calc_type = tk.Label(root, text="Standard",
                    font=("Helvetica", 15))
calc_type.place(x=30, y=0)
# calc_type.pack(padx=5, pady=5)

# Menu Button:

menu_button = tk.Button(root, text="M")
menu_button.place(x=0, y=0)




root.mainloop()