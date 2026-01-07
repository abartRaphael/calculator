from unittest import TestCase
from src.calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.mysum(1, 2), 3)

    def test_product(self):
        self.assertEqual(self.calc.myprod(2, 4), 8)

    
    
if __name__ == '__main__':
    unittest.main()
