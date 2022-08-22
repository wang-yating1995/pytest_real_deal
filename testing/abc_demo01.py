import pytest

def test_abc_demo01():
    assert 1==1

class LoginCase():
    def case_01(self):
        print("case_01")
    def test_01(self):
        print("test_01")
    def test_02(self):
        print("test_02")