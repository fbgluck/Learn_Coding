# Sample game part that fills a backpack with stuff

# Display the menu

# (0) Initialize the contents of the stash
stash = ["water",
         "food",
         "knife",
         "shoes",
         "flashlight",
         "shovel",
         "gun",
         "ammunition",
         "gold",
         "ax"
         ]
stashName = "the stash"
# Initialize the contents of the backpack
backpack = []
# Other Items Set Up
myName = input("Who is playing this adventure? ")
backpackName = myName + "'s " + "Backpack"

keepGoing = True

# ---------- Functions begin here
# function to list contents of backpack or stash


def listContents(theItem, itemName):
    i = 0  # initialize local variable for function
    if len(theItem) == 0:
        print(f"Sorry, {itemName} is empty :(")
    else:
        print(f"Here are the contents of the {itemName} as you requested:")
        for i in range(0, len(theItem)):
            print(f"{i+1}. {theItem[i]}")
    return (i)

# ---- This function is called to display a menu and ask for the user choice
# Arguments: - none -
# Returns: an integer that represents the choice made or -1 if a bad choice made


def displayMenu():
    choice_list = [1, 2, 3, 4, 0]  # List of valid choices
    print(f"(1) - What's in {backpackName} ")
    print(f"(2) - What's in {stashName}")
    print(f"(3) - Add something to {backpackName}")
    print(f"(4) - Remove something {backpackName}")
    print(f"(0) - End the adventure!")
    print(30*"-")
    menuChoice = (int(input("What do you want to do? ")))
    if menuChoice in choice_list:
        return menuChoice  # The function returns the item you chose
    else:
        # returning a negative value indicates the user did not make a correct slection
        return (-1)

# Transfer item from Stash to Backpack


def transferFromStash(itemNo):
    # Transfers the selected item from stash to Backpack
    # Check to see if this item is in the backpack
    if len(stash) > itemNo-1:
        selection = input(
            f"Are you sure you want to remove {stash[itemNo-1]} from the stash? y/n")
        if selection.lower == "y":
            print(f"Adding {stash[itemNo-1]} to your backpack")
            # Add it to the backpack
            backpack.append(stash(itemNo))
            # remove item from stash
            stash.pop(itemNo)
            # then list the backpack contents
            listContents(backpack, "backpack")
        else:
            # selection is not valid
            print(f"Please enter y or n")
    else:
        print("Sorry, the item you specified is not in the list")
        print("Please select an item between 1 and {(len(stash)+1)}")


# Game starts here
while keepGoing == True:  # Main Game Loop
    choice = displayMenu()  # Display the menu
    # We should make sure a valid choice was entered
    # Process the choice according to what was selected
    # --Menu choice 1 --
    if choice == 1:
        print(
            f"There are {listContents(backpack,'Backpack')} items in the backpack.")
    # -- Menu choice 2 --
    elif choice == 2:
        print(f"There are {listContents(stash,'Stash')+1} items in the stash.")
    # -- Menu choice 3 --
    elif choice == 3:
        listContents(stash, "Stash")
        selected_item = input(
            "Enter the number of the item you want to transfer >> ")
        transferFromStash(int(selected_item))
    elif choice == 0:
        # -- Menu choice END GAME --
        print("Thanks for playing....")
        keepGoing = False
    elif choice == -1:
        print("That is not a valid selection. Try again.")
        print(30*"-")
# End of Loop
print("Bye!! I hope you enjoyed your adventure!")


# (1) List the menu and the contents of the backpack and stash
# --- Menu ---
# (1) List the backpack contents
# (2) Transfer an item to from the stash to the backpack
# (2a) Check to see if the backpack is full
# (2b) If the backpack is not full remove the item from the stash
#      and add it to the backpack
# (3) List the new contents of the backpack
# (4) List the contents of the stash
# (5) End the game
