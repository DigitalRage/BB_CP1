# BB 1st Flexible Calculator Project

# Calculates the total of all numbers in the list
def calc_sum(numbers):
    return sum(numbers)

# Calculates the average by dividing the total by the number of items
def calc_average(numbers):
    return sum(numbers) / len(numbers)

# Finds the largest number in the list
def calc_max(numbers):
    return max(numbers)

# Finds the smallest number in the list
def calc_min(numbers):
    return min(numbers)

# Multiplies all numbers together to get the product
def calc_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Prompts the user to enter numbers one at a time
# Converts valid inputs to floats and adds them to a list
# Stops when the user types 'done'
def get_numbers():
    numbers = []
    print("\nEnter numbers (type 'done' when finished):")
    while True:
        entry = input("Number: ")
        if entry.lower() == "done":
            break
        try:
            number = float(entry)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return numbers

# Takes an operation name and a list of numbers as keyword arguments
# Calls the appropriate function based on the operation
# Displays the result to the user
def perform_operation(**kwargs):
    operation = kwargs.get("operation")
    numbers = kwargs.get("numbers", [])

    if not numbers:
        print("No numbers provided.")
        return

    print(f"\nCalculating {operation} of: {', '.join(map(str, numbers))}")

    if operation == "sum":
        result = calc_sum(numbers)
    elif operation == "average":
        result = calc_average(numbers)
    elif operation == "max":
        result = calc_max(numbers)
    elif operation == "min":
        result = calc_min(numbers)
    elif operation == "product":
        result = calc_product(numbers)
    else:
        print("Unsupported operation.")
        return

    print(f"Result: {result}")

# Main loop that runs the calculator
# Shows available operations and handles user interaction
# Repeats until the user chooses to exit
def run_calculator():
    print("Welcome to the Flexible Calculator!")
    print("\nAvailable operations: sum, average, max, min, product")

    while True:
        operation = input("\nWhich operation would you like to perform? ").lower()
        if operation not in ["sum", "average", "max", "min", "product"]:
            print("Invalid operation. Try again.")
            continue

        numbers = get_numbers()
        perform_operation(operation=operation, numbers=numbers)

        again = input("\nWould you like to perform another calculation? (yes/no) ").lower()
        if again != "yes":
            print("\nThank you for using the Flexible Calculator!")
            break

# Starts the calculator when the script runs
run_calculator()