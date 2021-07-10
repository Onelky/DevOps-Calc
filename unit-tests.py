import unittest
from unittest.main import main
from calc import Calculadora


class TestCal(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_suma(self):
        self.assertEqual(3, self.calc.sumar(1, 2))
        self.assertEqual(2002, self.calc.sumar(2, 2000))
        self.assertEqual(0, self.calc.sumar(0, 0))
        self.assertEqual(False, self.calc.sumar(-1, 0))

    def test_resta(self):
        self.assertEqual(0, self.calc.restar(2, 2))
        self.assertEqual(2000, self.calc.restar(4000, 2000))
        self.assertEqual(0, self.calc.restar(0, 0))
        self.assertEqual(False, self.calc.restar(-3, -4))

    def test_multiplicacion(self):
        self.assertEqual(14, self.calc.multiplicar(7, 2))
        self.assertEqual(0, self.calc.multiplicar(7, 0))
        self.assertEqual(False, self.calc.multiplicar(2, -5))
        self.assertEqual(100, self.calc.multiplicar(1, 100))

    def test_division(self):
        self.assertEqual(2, self.calc.division(2, 1))
        self.assertEqual(False, self.calc.division(0, -2))
        self.assertEqual(False, self.calc.division(1, 0))
        self.assertEqual(10, self.calc.division(100, 10))


if __name__ == "__main__":
    unittest.main()
