# Запуск тестов: python test_trg.py -v

# .assertEqual(a, b)	    a == b
# .assertTrue(x)	        bool(x) is True
# .assertFalse(x)	        bool(x) is False
# .assertIs(a, b)	        a is b
# .assertIsNone(x)	        x is None
# .assertIn(a, b)	        a in b
# .assertIsInstance(a, b)	isinstance(a, b)

import unittest
from triangle import prg
        
class Test(unittest.TestCase):
    def test_trg(self):
        prg.a = 12
        prg.b = 16
        prg.c = 50
        self.assertEqual(prg.is_triangle(), "Жаль, но из этого треугольник не сделать", "ne rabotaet")

if __name__ == '__main__':
    unittest.main()
