''' My Calculator Test'''

from calculator import add, subtract

def test_addition():
    '''Test that addition function works'''
    assert add (2,2) == 4

def test_subtraction():
    '''Test that subtraction function works'''
    assert subtract (2,2) == 0

def test_multiplication():
    '''Test that multiplication works'''
    assert test_multiplication (2,2) == 4

def test_division():
    '''Test that division works'''
    assert test_division (2,2) == 1