#Brian Day
#Version 1.4
# The purpose of this program is to allow the user to choose 5 products they would like to purchase with products each having their own prices and UPC codes, and when the user checks out the subtotal, tax, and grand total are calculated and displayed for the user.
print("Welcome to Brian's Goat Store, Where you \"always\" get more for your dollar. Your cart only holds five items, so choose carefully!")
shoppingCart = []
marketItems = ["50 Lb compressed hay bale", "8 Lb Goat mineral supplement", "8 Lb Himalayan Salt Block", "Pasteurized Goat Milk", "Water trough for goats", "Goat Milk Soap", "Goat Milk Coffee Creamer", "4 Pack of Goat Horns for Dogs", "Goat Hoof Trimmers", "Goat Dewormer"]
marketItemsPositions = ["50 Lb compressed hay bale", "8 Lb Goat mineral supplement", "8 Lb Himalayan Salt Block", "Pasteurized Goat Milk", "Water trough for goats", "Goat Milk Soap", "Goat Milk Coffee Creamer", "4 Pack of Goat Horns for Dogs", "Goat Hoof Trimmers", "Goat Dewormer"]
#        ^^ This list is used to match the price with the item in the reciept
marketUPC = ["184280000094", "095668956042", "840875087948", "00072904000202", "738633939465", "779242000955", "0063392471000", "671963025036", "680580280056", "662858488234"]
marketPrice = [23.48, 13.99, 25.42, 12.99, 45.99, 2.71, 18.99, 21.99, 9.99, 37.99]
priceLength = [5, 5, 5, 5, 5, 4, 5, 5, 4, 5]# The length of the price is used to make the UPC into columns.
#-------------------------------------------------------------------
def validChoice():
    global validChoices
    validChoices = []
    for i in range(len(marketItems)):
        validChoices.append(1 + len(validChoices))
    return validChoices
    #This function creates a range of valid choices based on the length of the amount of items still avalable to the user.
#-------------------------------------------------------------------
orderLoop = 0
while orderLoop < 6:#This limits the amount of times the user can purchase to 5
    for i in range(len(marketItems)):
        print(f"{i + 1} {marketItems[i]}", (30 - len(marketItems[i])) * " ", f"${marketPrice[i]}", (10 - priceLength[i]) * " ", f"UPC: {marketUPC[i]}")#This range and print function prints the name of the item, along with its price and UPC in straight columns.
    try:
        userChoice = int(input(f"\nWhat would you like to add to your cart?\nYour Choice (1-10): "))
    except:#   This code attempts to turn the user's input into an integer and returns an error if it is not.
        print("That's not a valid choice!")
        userActuallyBoughtSomething = False
        #Note - userActuallyBaughtSomething is a flag to make sure that the reciept only shows if the user chose an item to purchase.
    else:
        if userChoice in validChoice():
            print("------------------------------------------------------")
            print(f"You took the {marketItems[userChoice - 1]}!\n------------------------------------------------------")
            orderLoop = orderLoop + 1
            shoppingCart.append(marketItems[userChoice - 1])# This line adds the user's choice from marketItems to their shoppingCart
            marketItems.pop(userChoice - 1)# And this removes their choice from marketItems.
            userAnythingElse = input(("Would you like to add anything else to your cart? (yes/no) "))
            if userAnythingElse.lower() == "yes" and orderLoop < 5:# This makes sure that the user doesn't have the maximum number of items 
                print("Okay, here's a list of the items again.\n")
                userActuallyBoughtSomething = False
            elif userAnythingElse.lower() == "yes" and len(shoppingCart) == 5:
                 #If the user does have the maximum number of items, do this. ↓↓
                 print("\nYour cart is full! You sprint to the checkout.\nHere's your reciept:")
                 orderLoop = 6
                 userActuallyBoughtSomething = True
            elif userAnythingElse.lower() == "no":
                userActuallyBoughtSomething = True
                # userActuallyBaughtSomething is set to True since in order for them to get here they need to choose a product. 
                print("Okay, here's your reciept.\n")
                orderLoop = 6 #This allows the user to break out of the loop
            else:
                print("That's not a valid choice!")
        else:
            print("That's not a valid choice!")
    subtotal = 0.0
    for i in range(len(shoppingCart)):
        subtotal = subtotal + marketPrice[marketItemsPositions.index(shoppingCart[i])]
        #This adds the values of every item in the user's shoppingCart
    tax = ((2.5/100) * subtotal)
    grandTotal = tax + subtotal
if userActuallyBoughtSomething == True:
    print(f"------------------------------------------------------\nThank you for shopping Brian's GoatStore!\n1770 Main Street, Sanford, Maine")
    print("Your purchase:")
    for i in range(len(shoppingCart)):
        print(f"1x {shoppingCart[i]}", (30 - len(shoppingCart[i])) * " ", f"${marketPrice[marketItemsPositions.index(shoppingCart[i])]}", (10 - priceLength[i]) * " ", f"UPC: {marketUPC[i]}")
    print(f"\nsubtotal: ${round(subtotal,2)}\nTax: ${round(tax,2)}")
    print(f"Total: ${round(grandTotal,2)}")
    end = input("Insert cash or select payment type")
    #This final reciept shows the thank you message, subtotal, tax, and grand total for the user along with the items they purchased.