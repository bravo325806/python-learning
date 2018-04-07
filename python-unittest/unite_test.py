import  unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        # For example
        # result = calc.add(6,1)
        # self.assertEqual(result, 7)
        self.assertEqual(calc.add(-1,2), 1)
        self.assertEqual(calc.add(-1,-2), -3)
        self.assertEqual(calc.add(0,0), 0)

    def test_sub(self):
        self.assertEqual(calc.sub(-1,2), -3)
        self.assertEqual(calc.sub(-1,-2), 1)
        self.assertEqual(calc.sub(0,0), 0)

    def test_multi(self):
        self.assertEqual(calc.multi(-1,2), -2)
        self.assertEqual(calc.multi(-1,-2), 2)
        self.assertEqual(calc.multi(0,0), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(-1,2), -0.5)
        self.assertEqual(calc.divide(-1,-2), 0.5)
        
        # self.assertRaises(ValueError, calc.divide, 1, 0)
        with self.assertRaises(ValueError):
            calc.divide(1, 0)

if __name__ == '__main__':
    unittest.main()