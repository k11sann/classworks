# Запуск тестов: python test_realstring.py -v

# .assertEqual(a, b)	    a == b
# .assertTrue(x)	        bool(x) is True
# .assertFalse(x)	        bool(x) is False
# .assertIs(a, b)	        a is b
# .assertIsNone(x)	        x is None
# .assertIn(a, b)	        a in b
# .assertIsInstance(a, b)	isinstance(a, b)

import unittest
from RealString import rs
        
class Test(unittest.TestCase):
    def test_odd(self):
        self.assertEqual(rs.odd(), 1, "ne rabotaet")
        
    def test_odd_char(self):
        self.assertEqual(rs.odd_char(), 5983, "ne rabotaet")

if __name__ == '__main__':
    unittest.main()
