class CalculatorLogic:
    def __init__(self):
        self.expression = ""
        self.result_shown = False

    def add(self, char):
        if self.result_shown and char.isdigit():
            self.expression = ""
            self.result_shown = False
        self.expression += str(char)
        return self.expression

    def clear(self):
        self.expression = ""
        return self.expression

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.result_shown = True
            return self.expression
        except Exception:
            self.expression = ""
            self.result_shown = False
            return "Error"
