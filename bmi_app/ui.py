# ui.py
import tkinter as tk
from tkinter import messagebox
from logic import BMICalculator


class BMIApp:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator BMI")
        master.geometry("300x250")

        # Label
        tk.Label(master, text="Berat (kg):").pack(pady=5)
        self.weight_entry = tk.Entry(master)
        self.weight_entry.pack()

        tk.Label(master, text="Tinggi (cm):").pack(pady=5)
        self.height_entry = tk.Entry(master)
        self.height_entry.pack()

        # Tombol
        tk.Button(master, text="Hitung BMI",
                  command=self.calculate_bmi).pack(pady=10)
        tk.Button(master, text="Clear", command=self.clear).pack()

        # Hasil
        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            bmi_obj = BMICalculator(weight, height)

            bmi = bmi_obj.calculate_bmi()
            category = bmi_obj.category()

            self.result_label.config(text=f"BMI: {bmi} ({category})")

        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")

    def clear(self):
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.result_label.config(text="")
