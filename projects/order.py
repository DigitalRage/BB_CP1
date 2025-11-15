#BB 1st Order Up! Project
# Define the main course menu with categories and item prices
main_food = {
    "Burger": {
        "HamBurger": 10.00,
        "Cheeseburger": 10.00,
        "Big Mac Whopper": 10.00,
        "Double Double Chris Pratt Style": 10.00
    },
    "Mac and Cheese": {
        "Chinese Mac and Cheese": 10.00,
        "Mexican Mac and Cheese": 10.00,
        "American Mac and Cheese": 1000.00
    },
    "Tacos": {
        "Soft Tacos": 0.01,
        "Street Tacos": 10.00,
        "Delta Tacos": 1000.00
    }
}

# Define the drink menu with categories and item prices
drink_menu = {
    "Milkshakes": {
        "Chocolate Milkshake": 10.00,
        "Vanilla Milkshake": 10.00,
        "Strawberry Milkshake": 10.00,
        "The Mystery Milkshack": 1000.00
    },
    "Water": {
        "Tap Water": 100.00,
        "Fresh Water": 1000.00
    },
    "Geuse": {
        "Aypell Geuse": 10.00,
        "Aaronge Geuse": 10.00,
        "BeetleGeuse": 100000.00
    }
}

# Define the sides menu with item prices
side_menu = {
    "Mashed Potatoes": 10.00,
    "1000lb Fries": 0.01,
    "Salad": 1000000.00,
    "Bread": 10.00,
    "Onion Rings": 10.00
}

# Convert nested menu dictionaries into a flat dictionary with lowercase keys for easy matching
def normalize_menu(menu):
    flat = {}
    for category in menu.values():  # Loop through each category
        for item, price in category.items():  # Loop through each item in the category
            flat[item.lower()] = (item, price)  # Store lowercase version for lookup
    return flat

# Normalize all menu sections for case-insensitive input matching
main_items = normalize_menu(main_food)
drink_items = normalize_menu(drink_menu)
side_items = {item.lower(): (item, price) for item, price in side_menu.items()}

# Print the main course menu to the user
print("\nMain Courses")
for category, items in main_food.items():
    print(f"\n{category}")  # Print category name
    for item, price in items.items():
        print(f"{item} ::::::::: ${price:.2f}")  # Print item and price

# Print the drink menu to the user
print("\nDrinks")
for category, items in drink_menu.items():
    print(f"\n{category}")
    for item, price in items.items():
        print(f"{item} ::::::::: ${price:.2f}")

# Print the sides menu to the user
print("\nSides (Get at least 2 or die!)")
for item, price in side_menu.items():
    print(f"{item} ::::::::: ${price:.2f}")

# Ask the user for input until they enter a valid item from the menu
def get_valid_input(prompt, options):
    while True:
        choice = input(prompt).strip().lower()  # Get user input and normalize
        if choice in options:  # Check if input is valid
            return options[choice]  # Return the original item name and price
        else:
            print("Invalid choice. Try again.")
            print("Options include:")
            for name in options:
                print(f"- {options[name][0]}")  # Show valid options

# Initialize the order list and total cost
order = []
total = 0.0

# Ask the user to choose a main course
print("\nChoose your Main Course:")
main_choice, price = get_valid_input("Main: ", main_items)
order.append(main_choice)  # Add item to order
total += price  # Add price to total

# Ask the user to choose a drink
print("\nChoose your Drink:")
drink_choice, price = get_valid_input("Drink: ", drink_items)
order.append(drink_choice)
total += price

# Ask the user to choose at least two sides
print("\nChoose at least 2 Sides:")
side_count = 0
while side_count < 2:
    side_choice, price = get_valid_input(f"Side #{side_count + 1}: ", side_items)
    order.append(side_choice)
    total += price
    side_count += 1

# Ask the user if they want to add more sides
while True:
    more = input("Add another side? (yes/no): ").strip().lower()
    if more == "yes":
        side_choice, price = get_valid_input("Extra side: ", side_items)
        order.append(side_choice)
        total += price
    elif more == "no":
        break
    else:
        print("Please type 'yes' or 'no'.")

# Print the final order summary
print("\nYour Order Summary:")
for item in order:
    # Get the price from any of the menu sections
    price = main_items.get(item.lower(), (None, 0))[1] or \
            drink_items.get(item.lower(), (None, 0))[1] or \
            side_items.get(item.lower(), (None, 0))[1]
    print(f"- {item}: ${price:.2f}")

# Print the total cost of the order
print(f"\nTotal: ${total:.2f}")
