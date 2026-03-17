"""
GUI calculator built with tkinter.
Reuses core math functions from calculator.py.
"""

import tkinter as tk
from calculator import add, subtract, multiply, divide


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.resizable(False, False)

        self.current = ""
        self.first_number = None
        self.operation = None
        self.reset_next = False

        self._build_display()
        self._build_buttons()

    def _build_display(self):
        self.display_var = tk.StringVar(value="0")
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 28),
            justify="right",
            bd=0,
            bg="#f5f5f5",
            fg="#222222",
            state="readonly",
            readonlybackground="#f5f5f5",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=12, pady=12)

    def _build_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("−", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
        ]

        for (text, row, col) in buttons:
            self._make_button(text, row, col)

        equals = tk.Button(
            self.root,
            text="=",
            font=("Arial", 16, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=self._equals,
        )
        equals.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=8, pady=(0, 8), ipady=10)

    def _make_button(self, text, row, col):
        if text in ("÷", "×", "−", "+"):
            bg, fg = "#dbeafe", "#1e40af"
        elif text == "C":
            bg, fg = "#fee2e2", "#991b1b"
        else:
            bg, fg = "#f0f0f0", "#222222"

        cmd = {
            "C": self._clear,
            "÷": lambda: self._set_operation("÷"),
            "×": lambda: self._set_operation("×"),
            "−": lambda: self._set_operation("−"),
            "+": lambda: self._set_operation("+"),
            ".": self._decimal,
        }.get(text, lambda t=text: self._digit(t))

        btn = tk.Button(
            self.root,
            text=text,
            font=("Arial", 16),
            bg=bg,
            fg=fg,
            activebackground=bg,
            activeforeground=fg,
            bd=0,
            cursor="hand2",
            command=cmd,
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4, ipady=8)

        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1, minsize=70)
        for i in range(1, 6):
            self.root.grid_rowconfigure(i, weight=1)

    def _digit(self, text):
        if self.reset_next:
            self.current = ""
            self.reset_next = False
        self.current += text
        self.display_var.set(self.current)

    def _decimal(self):
        if self.reset_next:
            self.current = "0"
            self.reset_next = False
        if "." not in self.current:
            self.current += "." if self.current else "0."
            self.display_var.set(self.current)

    def _set_operation(self, op):
        if self.current:
            self.first_number = float(self.current)
            self.operation = op
            self.reset_next = True

    def _equals(self):
        if self.first_number is None or not self.operation or not self.current:
            return

        second = float(self.current)

        ops = {
            "+": add,
            "−": subtract,
            "×": multiply,
            "÷": divide,
        }

        result = ops[self.operation](self.first_number, second)
        self.display_var.set(result)
        self.current = str(result)
        self.first_number = None
        self.operation = None
        self.reset_next = True

    def _clear(self):
        self.current = ""
        self.first_number = None
        self.operation = None
        self.reset_next = False
        self.display_var.set("0")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()