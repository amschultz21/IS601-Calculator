from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a, b):
        calculation = a + b
        return calculation

    @staticmethod
    def subtract(a, b):
        calculation = a - b
        return calculation

    @staticmethod
    def multiply(a, b):
        calculation = a * b
        return calculation

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        calculation = a / b
        return calculation
