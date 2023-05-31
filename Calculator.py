import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.resizable(False, False)

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), width=5, padding=10)
        style.configure("TEntry", font=("Arial", 12), padding=10)

        self.entry = ttk.Entry(self.window)
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        for row_idx, row in enumerate(buttons):
            for col_idx, button_text in enumerate(row):
                ttk.Button(
                    self.window,
                    text=button_text,
                    command=lambda button_text=button_text: self.handle_button_click(button_text)
                ).grid(row=row_idx+1, column=col_idx, padx=5, pady=5)

        ttk.Button(
            self.window,
            text="Clear",
            command=self.clear_entry
        ).grid(row=len(buttons)+1, column=0, columnspan=4, padx=5, pady=5)

        self.window.mainloop()

    def handle_button_click(self, button):
        if button == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except (SyntaxError, ZeroDivisionError):
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + button)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    calculator = Calculator()
