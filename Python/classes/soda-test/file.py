# Запуск тестов: python file.py -v

# .assertEqual(a, b)	    a == b
# .assertTrue(x)	        bool(x) is True
# .assertFalse(x)	        bool(x) is False
# .assertIs(a, b)	        a is b
# .assertIsNone(x)	        x is None
# .assertIn(a, b)	        a in b
# .assertIsInstance(a, b)	isinstance(a, b)

import unittest
from SodaAlt import soda
        
class Test(unittest.TestCase):
    def test_equal1(self):
        soda.setType(1)
        self.assertEqual(soda.show_my_drink(), "ВИШНЁВАЯ", "ne rabotaet")
        
    def test_equal2(self):
        soda.setType(2)
        self.assertEqual(soda.show_my_drink(), "ЛИМОННАЯ", "ne rabotaet")
        
    def test_equal3(self):
        soda.setType(3)
        self.assertEqual(soda.show_my_drink(), "КОКИ КОЛА", "ne rabotaet")
    
    # описание тестов -->   

if __name__ == '__main__':
    unittest.main()
        
