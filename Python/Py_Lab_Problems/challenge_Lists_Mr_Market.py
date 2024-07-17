# This is the Mr. Market Problem.
""" The user needs to create a list with 10 items and a list
with 10 corresponding prices
The following is repeated three times:
- User chooses an item on the list
When the user has chosen three items, a receipt is printed
The first line of the receipt is a "Welcome" message
The following lines are the the name of each item, the price of each item
The last line of the item is total spent.
At the end of the receipt, a "Thank You For Shopping with us" message is printed
"""
# *** Define Functions ***


def show_list(which_list):
    # Show Contents of one of the lists
    # Parameters passed: the name of the list to be shown
    # Returns: nothing
    if which_list == "item":  # Show the items in the item_list
        print(f"\nYou can choose from the following items:")
        # Iterate through the lists. Print the items and their prices
        for i in range(0, len(item_list)):
            print(f"{item_list[i]:<15} $ {price_list[i]:<15.2f}")
    elif which_list == "receipt":  # Show the receipt
        print("\n\n========== TEAR HERE ===========")
        print(f"{'Welcome To Mr. Market':^30}")
        print(f"{'* Your Receipt *':^30}")
        print(30*"-")
        for i in range(0, len(cart_list)):
            # Prints the items and their prices
            print(f"{cart_list[i]:<15} {cart_price[i]:<15.2f}")
        print(f"\nYour total for all items is: $ {cart_total:.2f}\n ")
        # Print Message of the day at the bottom of the recipt
        print(f"{motd}\n\n")
        print(30*"-")
    else:  # show the cart list
        # handle the empty basket condition
        if len(cart_list) == 0:
            print(f"\nYour cart is currently empty\n")
        else:
            print(f"\nYour cart contains...")
            for i in range(0, len(cart_list)):
                print(f"{cart_list[i]:<15} $ {cart_price[i]:<15.2f}")

# Define Variables and Lists


cart_flag = True  # Used to control the while loop while customer chooses item from cart
cart_total = 0.00  # the running total of all items purchase
# The message of the day printed at the bottom of the receipt
motd = "Thank You For Shopping Mr. Market!"
# Create lists - 4 are required
# Create list for items
item_list = ["apples", "pears", "cherries", "banannas", "grapes", "lettuce"]
# Create corresponding list for prices
price_list = [.79, .51, 1.25, .49, 2.25, 1.30]
# Create item list for cart. Initially empty
cart_list = []
# Create item list for cart price. Initially empty
cart_price = []
#
#
# ***  Program starts here ****
print(f"{'Welcome To The Online Mr. Market':^30}")
print(30*'-')
# Repeat until user stops or all items have been purchased
while cart_flag and len(item_list) > 0:
    # Show user a menu of items available (with price)
    show_list("item")

    # Ask user to pick item and make sure that the input is all lower case
    buy_item = (input(
        "What would you like to purchase? (enter 'checkout' to checkout) > ")).lower()

    # Now check to make sure they choose an item that is available
    if buy_item != 'checkout':  # They entered an item and don't want to checkout
        if buy_item in item_list:  # check if the item entered is in the list
            # The item is available - find the position of the item in the list
            pos = item_list.index(buy_item)
            # remove the item from item_list because it is bought and no longer available
            item_list.pop(pos)
            # add the item to the cart since you just bought the item
            cart_list.append(buy_item)
            # add the price of the item to the item list
            # get the price from the price list
            current_price = price_list[pos]
            # remove the price from the price list so that the lists remain synced
            price_list.pop(pos)
            # add the item to the cart price list
            cart_price.append(current_price)
            # add the price to the cart_total (keeps the running total)
            cart_total = cart_total + current_price
            print(
                f"\n\nWe've added {buy_item} to your basket. You will be charged $ {current_price:.2f}")
            print(f"Your subtotal is: $ {cart_total:.2f}\n")

            show_list("cart\n")
        else:  # buy_item was not in the item list
            print(
                f"Sorry, that item is not available. Maybe you didn't enter it correctly?")
            print(f"If you want to checkout, enter 'checkout'")
    else:
        cart_flag = False  # User is finished choosing items or all items have been bought
# End While Loop

# Print receipt - The last thing done for the user. It's the end of their transaction.
show_list("receipt")

# End of Program
