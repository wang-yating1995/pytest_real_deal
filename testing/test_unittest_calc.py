import unittest
import sys

# print(sys.path)
sys.path.append("..")

from pytest_real_deal01.calc import Calc




class TestCal(unittest.TestCase):
    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1,2)
        self.assertEqual(3,result)

if __name__ == '__main__':
    unittest.main()