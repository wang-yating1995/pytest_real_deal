import string
from unicodedata import decimal

from pytest_real_deal01.calc import Calc
import pytest
from common.base_method import BaseMethod


class TestCalc():
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize(['a','b','c'],BaseMethod().open_yaml('..\data\calc_add_data.yml'))
    def test_add(self,a,b,c):
        try:
            result = self.calc.add(a, b)
            assert c == result
        except AssertionError as e1:
            result = round(result, 2)
            assert c == result
        except TypeError as e2:
            assert c == '类型错误：a,b不能为string类型'

    @pytest.mark.parametrize(['a', 'b', 'c'], BaseMethod().open_yaml('..\data\calc_sub_data.yml'))
    def test_sub(self,a,b,c):
        try:
            result = self.calc.sub(a, b)
            assert c == result
        except AssertionError as e1:
            result = round(result,2)
            assert c == result
        except TypeError as e2:
            assert c == '类型错误：a,b不能为string类型'

    @pytest.mark.parametrize(['a', 'b', 'c'], BaseMethod().open_yaml('..\data\calc_mul_data1.yml'))
    def test_mul(self,a,b,c):
        try:
            result = self.calc.mul(a, b)
            assert c == result
        except AssertionError as e1:
            result = round(result, 4)
            assert c == result
        except TypeError as e2:
            assert c == 'TypeError'

    @pytest.mark.parametrize(['a','b','c'],BaseMethod().open_yaml('../data/calc_div_data.yml'))
    def test_div(self,a,b,c):
        try:
            result = self.calc.div(a, b)
            assert c == result
        except AssertionError as e1:
            result = round(result, 4)
            assert c == result
        except TypeError as e2:
            assert c == 'TypeError'
        except ZeroDivisionError as e3:
            assert c == 'ZeroDivisionError'

if __name__ == '__main__':
    pytest.main()