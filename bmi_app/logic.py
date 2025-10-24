# bmi_logic.py

class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        try:
            bmi = self.weight / (self.height / 100) ** 2
            return round(bmi, 2)
        except ZeroDivisionError:
            return None

    def category(self):
        bmi = self.calculate_bmi()
        if bmi is None:
            return "Tinggi tidak boleh 0"
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Gemuk"
        else:
            return "Obesitas"
