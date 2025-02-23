import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

# Global command mapping for Calculator operations.
COMMANDS = {
    'add': Calculator.add,
    'subtract': Calculator.subtract,
    'multiply': Calculator.multiply,
    'divide': Calculator.divide
}

def print_menu():
    """Prints the available commands to the user."""
    print("Available commands:")
    for cmd in COMMANDS.keys():
        print(f"  - {cmd}")
    print("\nAdditional commands:")
    print("  - menu   : Display this menu")
    print("  - exit   : Exit the calculator")
    print("  - quit   : Exit the calculator")
    print()  # Blank line for readability.

def execute_command(command_line):
    """
    Parses a command line, converts number arguments to Decimal,
    and executes the corresponding Calculator operation.
    """
    tokens = command_line.strip().split()
    if not tokens:
        return  # Ignore empty input.

    command = tokens[0].lower()
    
    # Check for special commands.
    if command == "menu":
        print_menu()
        return

    if command in ("exit", "quit"):
        print("Exiting calculator.")
        sys.exit(0)

    if len(tokens) < 3:
        print("Usage: <command> <number1> <number2>")
        return

    try:
        a = Decimal(tokens[1])
        b = Decimal(tokens[2])
    except InvalidOperation:
        print("Invalid number input: please enter valid numbers.")
        return

    operation = COMMANDS.get(command)
    if not operation:
        print(f"Unknown command: {command}. Type 'menu' to see available commands.")
        return

    try:
        result = operation(a, b)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Non-interactive mode: if exactly three command-line arguments are provided.
    if len(sys.argv) == 4:
        # Expected usage: python calculator_main.py <number1> <number2> <operation>
        _, a, b, op = sys.argv
        command_line = f"{op} {a} {b}"
        execute_command(command_line)
    else:
        # Interactive mode: start the REPL.
        print("Welcome to the interactive calculator!")
        print_menu()
        while True:
            try:
                user_input = input("calc> ")
                execute_command(user_input)
            except (EOFError, KeyboardInterrupt):
                print("\nExiting calculator.")
                break

if __name__ == '__main__':
    main()
