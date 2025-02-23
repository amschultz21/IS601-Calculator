''' My Calculator Test'''

from calculator.calculation import Calculation  # Use the correct name

def test_addition():
    '''Test that addition function works'''
    calc = Calculation(2, 2, "add")
    assert calc.perform() == 4

def test_subtraction():
    '''Test that subtraction function works'''
    calc = Calculation(2, 2, "subtract")
    assert calc.perform() == 0

def test_multiplication():
    '''Test that multiplication function works'''
    calc = Calculation(2, 2, "multiply")
    assert calc.perform() == 4

def test_division():
    '''Test that division function works'''
    calc = Calculation(2, 2, "divide")
    assert calc.perform() == 1

def test_division_by_zero():
    '''Test division by zero returns None'''
    calc = Calculation(2, 0, "divide")
    assert calc.perform() is None  # Assuming division by zero returns None
