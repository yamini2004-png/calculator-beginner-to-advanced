import math

HISTORY_FILE = "History.txt"

# ---------------- HISTORY FUNCTIONS ---------------- #

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()

        if not lines:
            print("No History found!")
        else:
            for line in reversed(lines):
                print(line.strip())

    except FileNotFoundError:
        print("No History found!")

def clear_history():
    open(HISTORY_FILE, "w").close()
    print("History cleared.")

def save_to_history(expression, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{expression} = {result}\n")


# ---------------- CALCULATOR ENGINE ---------------- #

def calculate_basic(expression):
    """Handles + - * / ^ operations"""
    expression = expression.replace("^", "**")  # Power operator

    try:
        result = eval(expression)
        return int(result) if isinstance(result, float) and result.is_integer() else result

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except:
        return None


def calculate_scientific(parts):
    """Handles scientific functions: sin, cos, tan, sqrt, log"""
    func = parts[0].lower()

    if len(parts) != 2:
        return "Invalid scientific format. Example: sin 30"

    try:
        value = float(parts[1])
    except:
        return "Invalid number."

    if func == "sin":
        return round(math.sin(math.radians(value)), 4)
    elif func == "cos":
        return round(math.cos(math.radians(value)), 4)
    elif func == "tan":
        return round(math.tan(math.radians(value)), 4)
    elif func == "sqrt":
        return round(math.sqrt(value), 4)
    elif func == "log":
        return round(math.log10(value), 4)

    return None


# ---------------- MAIN FUNCTION ---------------- #

def main():
    print("\n--- ADVANCED PYTHON CALCULATOR ---")
    print("Type 'help' to see available commands.\n")

    while True:
        user_input = input("Enter expression or command: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        elif user_input.lower() == "help":
            print("""
Available Features:
-------------------
Basic Operators:
  5 + 3
  10 - 4
  6 * 7
  8 / 2
  2 ^ 5  (power)

Scientific:
  sin 30
  cos 60
  tan 45
  sqrt 25
  log 100

Commands:
  history - show previous calculations
  clear   - clear history
  exit    - quit calculator
""")
        else:
            parts = user_input.split()

            # Scientific function
            if len(parts) == 2 and parts[0].lower() in ["sin", "cos", "tan", "sqrt", "log"]:
                result = calculate_scientific(parts)
            else:
                # Basic Expression
                result = calculate_basic(user_input)
                if result is None:
                    print("Invalid expression.")
                    continue

            print("Result:", result)
            save_to_history(user_input, result)

# Run the calculator
if __name__ == "__main__":
    main()
