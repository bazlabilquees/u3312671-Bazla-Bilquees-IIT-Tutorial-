#Case Study — Student Marks Calculator (Functions + GUI)
import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        # Get marks from entries
        m1 = float(entry1.get())
        m2 = float(entry2.get())
        m3 = float(entry3.get())
        
        # Check if marks are within 0-100
        for m in (m1, m2, m3):
            if m < 0 or m > 100:
                messagebox.showerror("Invalid Input", "Marks must be between 0 and 100.")
                return
        
        # Calculate average
        avg = (m1 + m2 + m3) / 3
        
        # Determine Pass/Fail
        result = "Passed" if avg >= 50 else "Failed"
        
        # Show result
        output_label.config(text=f"Average: {avg:.2f} → {result}", fg="green" if result == "Passed" else "red")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Main window
root = tk.Tk()
root.title("Student Result Calculator")
root.geometry("350x250")

# Labels and entries
tk.Label(root, text="Enter 3 marks (out of 100):", font=("Arial", 16)).pack(pady=40)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Mark 1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(frame, width=10)
entry1.grid(row=0, column=1)

tk.Label(frame, text="Mark 2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(frame, width=10)
entry2.grid(row=1, column=1)

tk.Label(frame, text="Mark 3:").grid(row=2, column=0, padx=5, pady=5)
entry3 = tk.Entry(frame, width=10)
entry3.grid(row=2, column=1)

# Button
tk.Button(root, text="Calculate Result", command=calculate_result, bg="blue", fg="white").pack(pady=15)

# Output
output_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
output_label.pack(pady=10)

root.mainloop()
