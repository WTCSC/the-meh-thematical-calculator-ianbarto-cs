import new_calc
import pytest

#These test the addition calculation in order to make sure that it works properly

def test_add_two_positive_numbers():
    assert new_calc.add(1, 2) == 3

def test_add_two_negative_numbers():
    assert new_calc.add(-2, -3) == -5


# These tests make sure that subtracting works efficiently, and without any errors

def test_subtract_two_positive_numbers():
    assert new_calc.subtract(5, 3) == 2

def test_subtract_result_in_negative():
    assert new_calc.subtract(3, 5) == -2

def test_subtract_negative_and_positive_number():
    assert new_calc.subtract(-1, 1) == -2


# These tests make sure that multiplying is successfull, and that there are no errors when trying to multiply values

def test_multiply_two_positive_numbers():
    assert new_calc.multiply(5, 12) == 60

def test_multiply_two_negative_numbers():
    assert new_calc.multiply(-4, -5) == 20

def test_multiply_negative_and_positive_number():
    assert new_calc.multiply(-3, 4) == -12

def test_multiply_by_zero():
    assert new_calc.multiply(6767676767, 0) == 0



# This tests the division functions, making sure that you cant divide by zero, and that everything else is calculated correctly.


def test_divide_two_positive_numbers():
    assert new_calc.divide(8, 4) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        new_calc.divide(5, 0)

def test_exponent_two_positive_numbers():
    assert new_calc.exponent(2, 3) == 8

def test_add_negative_and_positive_number():
    assert new_calc.add(-1, 1) == 0
