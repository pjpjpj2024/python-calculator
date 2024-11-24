import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)  
        self.assertEqual(self.calc.add(-3, -7), -10)  
        
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5) 
        self.assertEqual(self.calc.subtract(-3, -7), 4)  

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)  
        self.assertEqual(self.calc.multiply(-3, 5), -15) 
        self.assertEqual(self.calc.multiply(0, 5), 0)  

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)  
        self.assertEqual(self.calc.divide(9, 3), 3)  
        self.assertRaises(ZeroDivisionError, self.calc.divide, 10, 0)  

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)  
        self.assertEqual(self.calc.modulo(10, 5), 0)  
        self.assertRaises(ZeroDivisionError, self.calc.modulo, 10, 0)  


if __name__ == '__main__':
    unittest.main()