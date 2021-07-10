class Calculadora:
    def sumar(self, num1, num2):
        if num1 < 0 or num2 < 0:
            return False
        return num1 + num2

    def restar(self, num1, num2):
        if num1 < 0 or num2 < 0:
            return False
        return num1 - num2

    def multiplicar(self, num1, num2):
        if num1 < 0 or num2 < 0:
            return False
        return num1 * num2

    def division(self, num1, num2):
        if num1 < 0 or num2 < 1:
            return False
        return int(num1 / num2)
