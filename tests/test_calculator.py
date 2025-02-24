''' My Calculator Test'''

from calculator.operations import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works'''
    assert add (2,2) == 4

def test_subtraction():
    '''Test that subtraction function works'''
    assert subtract (2,2) == 0

def test_multiplication():
    '''Test that multiply works'''
    assert multiply (2,2) == 4

def test_division():
    '''Test that division works'''
    assert divide (2,2) == 1
