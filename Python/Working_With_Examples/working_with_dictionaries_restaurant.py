# working_with_dictionaries_restaurant
# This system demonstrates the use of Python dictionaries
# and the use encoding a text to a value and decoding
# the value to a text.
#
# Python dictionaries create key/value pairs. Each key in a dictionary must be unique
# The value is "encoded" by the key.
#
# Define a dictionary. Each key value represents a meal choice
# Here we are encoding a meal choice as a number
meal_choices = {
    1: "Hamburger and Fries",
    2: "Fried Clam Dinner",
    3: "Top Shelf Sub",
    4: "Spinach and Cheese Calzone",
    5: "Individual Pineapple Pizza"
}

print(f"Welcome to Zeros. Here's what the chef is serving today.")
print(40*"=")
for i in range(1, len(meal_choices)+1):
    print(f"Choose {i} for {meal_choices[i]}")
item_number = int(input("\nWhat item number can I get for you today? "))
print(40*"=")
if item_number in meal_choices:
    # Here, we are decoding number to a meal choice
    print(f"OK... {meal_choices[item_number]} coming right up!")
else:
    print(f"Sorry, we don't have a number {item_number} on the menu")
# End of execution
print(2*"\n\n")
