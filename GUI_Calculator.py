# #welcoming
# print("Welcome to the calculator!\n")
#
# #loop
# while True:
#     try:
#         #user options
#         print("choose what do you want;\nAdd\nSub\nMultiplication\nDivision\nExponent".capitalize())
#         user = str(input("Enter your choice: \n")).lower()
#         #user input
#         a = int(input("Enter your first number: "))
#         b = int(input("Enter your second  number: "))
#
#         #conditions for the operations
#         if user == "add":
#             print(a + b)
#         elif user == "sub":
#             print(a - b)
#         elif user == "multiplication":
#             print(a * b)
#         elif user == "division":
#             if b == 0:
#                 print("\nNot Defined!".upper())
#             else:
#                 print(a/b)
#         elif user == "exponent":
#             print(a ** b)
#         elif user == "multiplication" or user == "multi":
#             print(a * b)
#         else:
#             print("Please enter a invalid choice.")
#
#         print("\n")
#
#     except ValueError:
#         print("Value Error: Sorry You've Entered Wrong Input :(".upper())
#         break

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        user = operation.get().lower()

        if user == "add":
            result.set(a + b)
        elif user == "sub":
            result.set(a - b)
        elif user in ("multiplication", "multi"):
            result.set(a * b)
        elif user == "division":
            if b == 0:
                messagebox.showerror("Error", "Division by Zero is NOT DEFINED!")
            else:
                result.set(a / b)
        elif user == "exponent":
            result.set(a ** b)
        elif user in ("remainder", "%"):
            if b == 0:
                messagebox.showerror("Error", "Division by Zero is NOT DEFINED!")
            else:
                result.set(a % b)
        else:
            messagebox.showerror("Error", "Invalid choice! Please try again.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("420x400")
root.config(bg="#1e1e1e")  # Dark background

# Styling
label_fg = "#ffffff"
entry_bg = "#2d2d2d"
entry_fg = "#ffffff"
button_bg = "#3a3a3a"
button_fg = "#ffffff"

# Labels and Entries
tk.Label(root, text="Welcome to the Calculator!", font=("Arial", 16, "bold"), bg="#1e1e1e", fg=label_fg).pack(pady=5)

tk.Label(root, text="First Number:", bg="#1e1e1e", fg=label_fg).pack()
entry_a = tk.Entry(root, bg=entry_bg, fg=entry_fg, insertbackground="white")
entry_a.pack()

tk.Label(root, text="Second Number:", bg="#1e1e1e", fg=label_fg).pack()
entry_b = tk.Entry(root, bg=entry_bg, fg=entry_fg, insertbackground="white")
entry_b.pack()

tk.Label(root, text="Operation (Add, Sub, Multiplication, Division, Exponent, Remainder):", bg="#1e1e1e", fg=label_fg).pack()
operation = tk.Entry(root, bg=entry_bg, fg=entry_fg, insertbackground="white")
operation.pack()

# Calculate Button
tk.Button(root, text="Calculate", command=calculate, bg=button_bg, fg=button_fg).pack(pady=10)

# Result Display
result = tk.StringVar()
tk.Label(root, text="Result:", font=("Arial", 12, "bold"), bg="#1e1e1e", fg=label_fg).pack()
tk.Label(root, textvariable=result, font=("Arial", 14), bg="#1e1e1e", fg="#00ff99").pack()

# Author credit
tk.Label(root, text="Created by: Himesh Gupta | Class 11th 'A'", font=("Arial", 9, "italic"), bg="#1e1e1e", fg="#888888").pack(side="bottom", pady=10)

# Run GUI
root.mainloop()
