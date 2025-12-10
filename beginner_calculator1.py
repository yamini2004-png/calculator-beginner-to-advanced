HISTORY_FILE = "History.txt"

def show_history():
    try:
        file = open(HISTORY_FILE, 'r')
        lines = file.readlines()
        file.close()

        if len(lines) == 0:
            print("No History found!")
        else:
            for line in reversed(lines):
                print(line.strip())
    except FileNotFoundError:
        print("No History found!")

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("History cleared.")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use: number operator number (e.g. 8 + 8)")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use only + - * /")
        return

    if result.is_integer():
        result = int(result)

    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print("--- Simple Calculator (type history, clear, exit) ---")
    while True:
        user_input = input("Enter expression or command: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)

main()
