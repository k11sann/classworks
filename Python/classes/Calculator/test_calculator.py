# Запуск тестов: python test_calculator.py -v

# .assertEqual(a, b)	    a == b
# .assertTrue(x)	        bool(x) is True
# .assertFalse(x)	        bool(x) is False
# .assertIs(a, b)	        a is b
# .assertIsNone(x)	        x is None
# .assertIn(a, b)	        a in b
# .assertIsInstance(a, b)	isinstance(a, b)

import unittest
from calculator import calc
        
class Test(unittest.TestCase):
    def test_calc_sum(self):
        calc.num1=30
        self.assertEqual(calc.calc_sum(60), 90, "ne rabotaet")
        
    def test_calc_multiply(self):
        calc.num1=9
        self.assertEqual(calc.calc_multiply(3), 27, "ne rabotaet")
        
    def test_calc_subtract(self):
        calc.num1=90
        self.assertEqual(calc.calc_subtract(6), 84, "ne rabotaet")
        
    def test_calc_divide(self):
        calc.num1=90
        self.assertEqual(calc.calc_divide(30), 3, "ne rabotaet")
    
    # описание тестов -->   

if __name__ == '__main__':
    unittest.main()
        
