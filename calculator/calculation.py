class Calculation:
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def perform(self):
        if self.operation == "add":
            return self.num1 + self.num2
        elif self.operation == "subtract":
            return self.num1 - self.num2
        elif self.operation == "multiply":
            return self.num1 * self.num2
        elif self.operation == "divide":
            return self.num1 / self.num2 if self.num2 != 0 else None
        else:
            raise ValueError("Invalid operation")
