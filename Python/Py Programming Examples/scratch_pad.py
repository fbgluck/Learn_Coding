# This is my program
# Author: Shawn Christian
# Version 1.0
# --------------
# VS Code and the Python Compiler.
#-----------------------------------------------
# Class: is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. 
# Enumerate: a function that is used to loop over an iterable while keeping track of the index of each element.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Define a class to represent each item
class Item:
    # Initialize an item with its UPC, name, price, and taxable status
    def __init__(self, upc, name, price, taxable):
        self.upc = upc  # Unique Product Code
        self.name = name  # Product name
        self.price = price  # Product price
        self.taxable = taxable  # Whether the product is taxable

# Define a class to manage the shopping cart
class ShoppingCart:
    # Initialize an empty shopping cart
    def __init__(self):
        self.items = []  # List of items in the cart

    # Add an item to the cart
    def add_item(self, item):
        self.items.append(item)

    # Display the current cart contents
    def view_cart(self):
        print("Current Cart:")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. UPC: {item.upc}, Name: {item.name}, Price: ${item.price:.2f}")
        print()

    # Process the checkout and print a receipt
    def checkout(self):
        # Calculate the subtotal and tax
        subtotal = 0
        tax = 0
        for item in self.items:
            subtotal += item.price
            if item.taxable:
                tax += item.price * 0.025

        # Print the receipt
        print("Receipt:")
        print("--------")
        print("Welcome to Mr. Market!")
        print()
        print("Selected Items:")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. UPC: {item.upc}, Name: {item.name}, Price: ${item.price:.2f}")
        print()
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax ({2.5}%): ${tax:.2f}")
        print(f"Grand Total: ${subtotal + tax:.2f}")
        print("Thank you for shopping at Mr. Market!")

# Predefined list of items
items = [
    Item("1234567890", "Apple", 1.99, True),
    Item("0987654321", "Banana", 0.99, False),
    Item("1111111111", "Orange", 2.49, True),
    Item("2222222222", "Grapes", 3.99, False),
    Item("3333333333", "Milk", 4.99, True),
    Item("4444444444", "Bread", 2.99, False),
    Item("5555555555", "Eggs", 1.99, True),
    Item("6666666666", "Chicken", 6.99, False),
    Item("7777777777", "Steak", 9.99, True),
    Item("8888888888", "Salmon", 12.99, False),
]

# Create a shopping cart
cart = ShoppingCart()

# Main program loop
while True:
    # Display the menu
    print("Menu:")
    print("1. View Cart")
    print("2. Add Item to Cart")
    print("3. Checkout")
    print("4. Exit")
    choice = input("Choose an option: ")

    # Handle the user's choice
    if choice == "1":
        # Display the current cart contents
        cart.view_cart()
    elif choice == "2":
        # Display the available items
        print("Available Items:")
        for i, item in enumerate(items, start=1):
            print(f"{i}. UPC: {item.upc}, Name: {item.name}, Price: ${item.price:.2f}")
        # Get the user's choice
        choice = input("Choose an item to add to cart (enter the number): ")
        try:
            # Validate the user's choice
            choice = int(choice)
            if 1 <= choice <= len(items):
                # Add the item to the cart
                cart.add_item(items[choice - 1])
                print(f"Added {items[choice - 1].name} to cart.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")
    elif choice == "3":
        # Process the checkout and print a receipt
        cart.checkout()
        break
    elif choice == "4":
        # Exit the program
        print("Goodbye!")
        break
    else:
        # Handle invalid choices
        print("Invalid choice.")