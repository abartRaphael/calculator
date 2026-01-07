from unittest import TestCase
from src.calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.sum(1, 2), 3)

    def test_max(self):
        self.assertEqual(self.calc.mymax(3,5), 5)
        
    def test_product(self):
        self.assertEqual(self.calc.prod(2, 4), 8)

    
    
if __name__ == '__main__':
    unittest.main()
