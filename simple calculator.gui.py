import tkinter as tk
from tkinter import messagebox
import math

# Define the main calculator class
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(0, 0)
        
        # Memory to store intermediate values
        self.memory = 0

        self.create_widgets()
    
    def create_widgets(self):
        # Entry widget to display input/output
        self.entry = tk.Entry(self, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sqrt', 'x^y', 'C', 'M+'
        ]

        row = 1
        col = 0

        for button in buttons:
            if button == "=":
                tk.Button(self, text=button, font=("Arial", 18), command=self.calculate).grid(row=row, column=col, columnspan=2, sticky="we")
                col += 2
            elif button == "C":
                tk.Button(self, text=button, font=("Arial", 18), command=self.clear).grid(row=row, column=col, sticky="we")
            elif button == "sqrt":
                tk.Button(self, text=button, font=("Arial", 18), command=self.sqrt).grid(row=row, column=col, sticky="we")
            elif button == "x^y":
                tk.Button(self, text=button, font=("Arial", 18), command=self.exponentiation).grid(row=row, column=col, sticky="we")
            elif button == "M+":
                tk.Button(self, text=button, font=("Arial", 18), command=self.memory_add).grid(row=row, column=col, sticky="we")
            else:
                tk.Button(self, text=button, font=("Arial", 18), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col, sticky="we")

            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        current_text = self.entry.get()
        new_text = current_text + char
        self.entry.delete(0, tk.END)
        self.entry.insert(0, new_text)

    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed")
            self.entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.entry.delete(0, tk.END)

    def sqrt(self):
        try:
            number = float(self.entry.get())
            result = math.sqrt(number)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for square root")
            self.entry.delete(0, tk.END)

    def exponentiation(self):
        current_text = self.entry.get()
        new_text = current_text + "**"
        self.entry.delete(0, tk.END)
        self.entry.insert(0, new_text)

    def memory_add(self):
        try:
            self.memory += float(self.entry.get())
            self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for memory add")
            self.entry.delete(0, tk.END)

# Run the application
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
