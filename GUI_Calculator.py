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
        else:
            messagebox.showerror("Error", "Invalid choice! Please try again.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x350")

# Labels and Entries
tk.Label(root, text="Welcome to the Calculator!", font=("Arial", 15, "bold")).pack(pady=5)

tk.Label(root, text="First Number:").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Second Number:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Operation (Add, Sub, Multiplication, Division, Exponent):").pack()
operation = tk.Entry(root)
operation.pack()

# Calculate Button
tk.Button(root, text="Calculate", command=calculate, bg="lightblue").pack(pady=5)

# Result Display
result = tk.StringVar()
tk.Label(root, text="Result:", font=("Arial", 10, "bold")).pack()
tk.Label(root, textvariable=result, font=("Arial", 12)).pack()

# Run GUI
root.mainloop()