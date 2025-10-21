import tkinter as tk
from ui import CalculatorUI


def main():
    root = tk.Tk()
    root.geometry("350x400")
    CalculatorUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
