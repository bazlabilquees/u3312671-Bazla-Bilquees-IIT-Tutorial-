##Case Study — Student Marks Calculator (Functions + GUI) with extension
import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        # Read marks (split by space or comma)
        marks_input = entry_marks.get().replace(",", " ").split()
        marks = [float(m) for m in marks_input]

        # Validate marks
        for m in marks:
            if m < 0 or m > 100:
                messagebox.showerror("Invalid Input", "Marks must be between 0 and 100.")
                return
        
        if not marks:
            messagebox.showerror("Invalid Input", "Please enter at least one mark.")
            return

        # Calculate average
        avg = sum(marks) / len(marks)

        # Determine Pass/Fail
        result = "Passed" if avg >= 50 else "Failed"

        # Update result label + background
        output_label.config(text=f"Average: {avg:.2f} → {result}")
        root.config(bg="lightgreen" if result == "Passed" else "lightcoral")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def clear_fields():
    entry_marks.delete(0, tk.END)
    output_label.config(text="")
    root.config(bg="SystemButtonFace")  # reset background

# Main window
root = tk.Tk()
root.title("Student Result Calculator")
root.geometry("400x250")

# Label + entry
tk.Label(root, text="Enter marks (separated by space or comma):", font=("Arial", 12)).pack(pady=10)

entry_marks = tk.Entry(root, width=40)
entry_marks.pack(pady=5)

# Buttons frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Calculate Result", command=calculate_result, bg="blue", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_fields, bg="gray", fg="white").grid(row=0, column=1, padx=5)

# Output
output_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
output_label.pack(pady=15)

root.mainloop()
