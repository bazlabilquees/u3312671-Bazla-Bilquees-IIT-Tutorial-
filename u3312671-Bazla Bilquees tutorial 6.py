import tkinter as tk
from tkinter import simpledialog

def greet():
    # Ask for the name in a popup
    name = simpledialog.askstring("Input", "What is your name?")
    # Update the label with greeting
    output.config(text=f"Hello, {name or 'friend'}!")

root = tk.Tk()
root.title("Greeter")

# Button to trigger greeting
btn = tk.Button(root, text="Click me", command=greet)
btn.pack(pady=10)

# Label to display the greeting
output = tk.Label(root, text="", font=("Arial", 12))
output.pack(pady=5)

root.mainloop()
