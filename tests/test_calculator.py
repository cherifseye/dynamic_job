import pytest
from src.calculator import dumy_calculator

@pytest.fixture
def calculator():
    return dumy_calculator()

def test_add(calculator):
    result = calculator.add(2, 3)
    assert result == 5

def test_add_negative_numbers(calculator):
    result = calculator.add(-5, -3)
    assert result == -8

def test_subs(calculator):
    result = calculator.subs(5, 3)
    assert result == 2

def test_subs_negative_result(calculator):
    result = calculator.subs(3, 5)
    assert result == -2

def test_mul(calculator):
    result = calculator.mul(2, 3)
    assert result == 6

def test_mul_with_zero(calculator):
    result = calculator.mul(5, 0)
    assert result == 0
