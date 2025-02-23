import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def execute_command(command_line):
    """
    Parses a command line, converts the arguments to Decimal,
    and executes the corresponding Calculator operation.
    """
    tokens = command_line.strip().split()
    if not tokens:
        return  # Empty input; do nothing.

    # Get the command (operation) and allow quitting.
    command = tokens[0].lower()
    if command in ("exit", "quit"):
        print("Exiting calculator.")
        sys.exit(0)

    if len(tokens) < 3:
        print("Usage: <command> <number1> <number2>")
        return

    # Try to convert number arguments to Decimal.
    try:
        a = Decimal(tokens[1])
        b = Decimal(tokens[2])
    except InvalidOperation:
        print("Invalid number input: please enter valid numbers.")
        return

    # Command pattern: map commands to Calculator methods.
    command_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    operation = command_mappings.get(command)
    if not operation:
        print(f"Unknown command: {command}. Valid commands are add, subtract, multiply, divide.")
        return

    try:
        result = operation(a, b)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Non-interactive mode: use command-line arguments if provided.
    if len(sys.argv) == 4:
        # Expected usage: python calculator_main.py <number1> <number2> <operation>
        _, a, b, op = sys.argv
        command_line = f"{op} {a} {b}"
        execute_command(command_line)
    else:
        # REPL mode: interactive loop.
        print("Welcome to the interactive calculator!")
        print("Enter commands in the format: <operation> <number1> <number2>")
        print("Supported operations: add, subtract, multiply, divide")
        print("Type 'exit' or 'quit' to exit.")
        while True:
            try:
                user_input = input("calc> ")
                execute_command(user_input)
            except (EOFError, KeyboardInterrupt):
                print("\nExiting calculator.")
                break

if __name__ == '__main__':
    main()
