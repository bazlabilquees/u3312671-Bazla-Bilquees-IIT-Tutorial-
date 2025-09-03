import tkinter as tk

def say_hello():
    print("Hello from the button!")

root = tk.Tk()
root.title("Callbacks")
root.geometry("320x160")

btn = tk.Button(root, text="Click me", command=say_hello)
btn.pack(pady=10)

root.mainloop()
