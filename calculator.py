 calculator.py
# A simple command-line (CMD) calculator.
# Each arithmetic operation lives in its own function, and the program keeps
# running inside a while loop until the sentinel variable is set to False.


import os


# ---------------------------------------------------------------------------
# Arithmetic functions
# Each function takes two numbers and returns the result of one operation.
# ---------------------------------------------------------------------------

def add(a, b):
    # Returns the sum of a and b.
    return a + b


def subtract(a, b):
    # Returns b subtracted from a.
    return a - b


def multiply(a, b):
    # Returns the product of a and b.
    return a * b


def divide(a, b):
    # Returns a divided by b.
    # Division by zero is not allowed, so we return a message instead of crashing.
    if b == 0:
        return "Error: cannot divide by zero."
    return a / b


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def clear_output():
    # Clears the terminal window so the user can start with a clean screen.
    # "cls" is the Windows (CMD) command, "clear" is used on Linux/macOS.
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    # Prints the list of options the user can choose from.
    print("=" * 34)
    print("        SIMPLE CALCULATOR")
    print("=" * 34)
    print("  +  Addition")
    print("  -  Subtraction")
    print("  *  Multiplication")
    print("  /  Division")
    print("  c  Clear the output")
    print("  q  Quit the program")
    print("=" * 34)


def get_number(prompt):
    # Asks the user for a number and keeps asking until valid input is given.
    # float() is used so decimal numbers are also accepted.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That is not a valid number. Please try again.")


# ---------------------------------------------------------------------------
# Main program
# The sentinel variable "running" controls the loop. It stays True while the
# calculator should keep working, and is set to False when the user quits.
# ---------------------------------------------------------------------------

def main():
    running = True  # sentinel variable used to exit the loop

    clear_output()

    while running:
        show_menu()
        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            # Set the sentinel to False so the loop stops on the next check.
            running = False
            print("Goodbye!")

        elif choice == "c":
            # Wipe the screen and show the menu again on the next pass.
            clear_output()

        elif choice in ("+", "-", "*", "/"):
            # Collect the two numbers the operation needs.
            first = get_number("Enter the first number:  ")
            second = get_number("Enter the second number: ")

            # Call the matching function for the chosen operation.
            if choice == "+":
                answer = add(first, second)
            elif choice == "-":
                answer = subtract(first, second)
            elif choice == "*":
                answer = multiply(first, second)
            else:
                answer = divide(first, second)

            print(f"\nResult: {first} {choice} {second} = {answer}\n")

        else:
            # Anything that is not a listed option is rejected.
            print("\nUnknown option. Please choose one from the menu.\n")


# Only run the calculator when this file is executed directly,
# not when it is imported into another program.
if __name__ == "__main__":
    main()