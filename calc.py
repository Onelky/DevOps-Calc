class Calculadora:
    def sumar(self, num1, num2):
        if num1 < 0 or num2 < 0:
            return False
        return num1 + num2
