from tkinter import simpledialog

# Prompts for text input
user_name = simpledialog.askstring("Input", "What is your name?")

# Prompts for an integer (validates that it's a number within the bounds)
user_age = simpledialog.askinteger("Input", "Enter your age:", minvalue=1, maxvalue=120)

# Prompts for a floating-point number
user_height = simpledialog.askfloat("Input", "Enter your height in meters:")
