import tkinter as tk
from tkinter import ttk
from logic import CalculatorLogic


class CalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator")
        self.logic = CalculatorLogic()
        self.create_widgets()

    def create_widgets(self):
        self.entry = ttk.Entry(self.root, font=(
            "Consolas", 20), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4,
                        sticky="nsew", padx=5, pady=5)

        buttons = [
            ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2)
        ]

        for (text, row, col) in buttons:
            if text == "=":
                btn = ttk.Button(self.root, text=text, command=self.calculate)
                btn.grid(row=row, column=col, columnspan=2,
                         sticky="nsew", padx=2, pady=2)
            elif text == "C":
                btn = ttk.Button(self.root, text=text, command=self.clear)
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            else:
                btn = ttk.Button(self.root, text=text,
                                 command=lambda t=text: self.add_char(t))
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for j in range(4):
            self.root.columnconfigure(j, weight=1)

    def add_char(self, char):
        result = self.logic.add(char)
        self.update_display(result)

    def clear(self):
        result = self.logic.clear()
        self.update_display(result)

    def calculate(self):
        result = self.logic.calculate()
        self.update_display(result)

    def update_display(self, text):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, text)
