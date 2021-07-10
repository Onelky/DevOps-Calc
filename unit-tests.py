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


if __name__ == "__main__":
    unittest.main()
