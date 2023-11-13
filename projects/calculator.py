import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == 'Addition':
        result = add(num1, num2)
    elif operation == 'Subtraction':
        result = subtract(num1, num2)
    elif operation == 'Multiplication':
        result = multiply(num1, num2)
    elif operation == 'Division':
        result = divide(num1, num2)
    else:
        result = "Invalid operation"

    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widgets for input numbers
entry_num1 = tk.Entry(root, width=20)
entry_num1.grid(row=0, column=0, padx=40, pady=40)

entry_num2 = tk.Entry(root, width=20)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for selecting operation
operations = ['Addition', 'Subtraction', 'Multiplication', 'Division']
operation_var = tk.StringVar(root)
operation_var.set(operations[0])  # Default value
operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.grid(row=0, column=2, padx=30, pady=30)

# Button to perform calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=0, columnspan=3, pady=10)

# Run the main loop
root.mainloop()
