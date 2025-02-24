import sys
import pytest
from decimal import Decimal
import calculator_main  # This is your main module with the REPL and command pattern code

# Import the functions and global variables to test.
from calculator_main import execute_command, print_menu, COMMANDS, main

def test_execute_command_valid_add(capsys):
    execute_command("add 2 3")
    captured = capsys.readouterr().out
    assert "Result: 5" in captured

def test_execute_command_valid_subtract(capsys):
    execute_command("subtract 5 2")
    captured = capsys.readouterr().out
    assert "Result: 3" in captured

def test_execute_command_valid_multiply(capsys):
    execute_command("multiply 4 3")
    captured = capsys.readouterr().out
    assert "Result: 12" in captured

def test_execute_command_valid_divide(capsys):
    execute_command("divide 10 2")
    captured = capsys.readouterr().out
    assert "Result: 5" in captured

def test_execute_command_unknown_command(capsys):
    execute_command("mod 10 3")
    captured = capsys.readouterr().out
    assert "Unknown command" in captured

def test_execute_command_invalid_numbers(capsys):
    execute_command("add a 3")
    captured = capsys.readouterr().out
    assert "Invalid number input" in captured

def test_execute_command_division_by_zero(capsys):
    execute_command("divide 10 0")
    captured = capsys.readouterr().out
    assert "Division by zero" in captured

def test_execute_command_menu(capsys):
    execute_command("menu")
    captured = capsys.readouterr().out
    # Ensure that the menu lists all commands from the global COMMANDS dictionary.
    for cmd in COMMANDS.keys():
        assert cmd in captured

def test_execute_command_empty_input(capsys):
    execute_command("")
    captured = capsys.readouterr().out
    # No output should be produced for empty input.
    assert captured == ""

def test_exit_command(monkeypatch):
    # Override sys.exit to raise a SystemExit exception.
    monkeypatch.setattr(sys, "exit", lambda code: (_ for _ in ()).throw(SystemExit(code)))
    with pytest.raises(SystemExit):
        execute_command("exit")
    with pytest.raises(SystemExit):
        execute_command("quit")

def test_main_non_interactive(monkeypatch, capsys):
    # Simulate non-interactive mode by providing exactly 4 sys.argv items.
    test_args = ["calculator_main.py", "2", "3", "add"]
    monkeypatch.setattr(sys, "argv", test_args)
    # Call main; it should run the non-interactive command.
    calculator_main.main()
    captured = capsys.readouterr().out
    assert "Result: 5" in captured

def test_main_interactive(monkeypatch, capsys):
    # Simulate interactive mode by setting sys.argv with fewer than 4 arguments.
    monkeypatch.setattr(sys, "argv", ["calculator_main.py"])
    # Create an iterator that simulates user input: first a valid command, then an exit command.
    inputs = iter(["add 2 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    # The REPL loop should eventually call sys.exit when "exit" is entered.
    with pytest.raises(SystemExit):
        calculator_main.main()
    captured = capsys.readouterr().out
    assert "Result: 5" in captured
    assert "Exiting calculator." in captured
