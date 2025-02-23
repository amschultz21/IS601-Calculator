import sys
import os
import importlib.util
from calculator import Calculator
from decimal import Decimal, InvalidOperation

# Global command mapping for Calculator operations.
COMMANDS = {
    'add': Calculator.add,
    'subtract': Calculator.subtract,
    'multiply': Calculator.multiply,
    'divide': Calculator.divide
}

def load_plugins(commands):
    """Automatically load plugins from a 'plugins' directory and register their commands."""
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    if not os.path.isdir(plugins_dir):
        return  # No plugins folder found, nothing to load.
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            filepath = os.path.join(plugins_dir, filename)
            module_name = os.path.splitext(filename)[0]
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            # If the module defines a register_command function, call it.
            if hasattr(module, 'register_command'):
                module.register_command(commands)

def print_menu():
    """Prints the available commands to the user."""
    print("Available commands:")
    for cmd in sorted(COMMANDS.keys()):
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
    # Load plugins to extend the commands dictionary.
    load_plugins(COMMANDS)

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
