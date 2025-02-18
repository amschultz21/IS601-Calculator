from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add (a,b):
        calculation = calculation(a, b, add)
        return calculation.get_result()
    @staticmethod
    def subtract (a,b):
        calculation = calculation(a, b, subtract)
        return calculation.get_result()
    @staticmethod
    def multiply (a,b):
        calculation = calculation(a, b, multiply)
        return calculation.get_result()
    @staticmethod
    def divide (a,b):
        calculation = calculation(a, b, divide)
        return calculation.get_result()