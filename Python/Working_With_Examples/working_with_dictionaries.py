#  Examples of how to use a dictionary in Python
#  Dictionaries are defined with key:value pairs (note comma)
#  Keys can be integers or strings
test_dict = {
    1: "one",
    2: "two",
    3: "three"
}
# We retrieve items from a dictionary using the dictionary
# name and specifying a key
print("*** Return the value with the key of 2")
print(test_dict[2])

# iterating through a dict with a loop
print("Iterate through specific items in a dictionary  with a loop")
for i in range(1, 3):  # start at 1 stop before 3
    print(test_dict[i])



# ----------------------

# Methods used with Dictionaries
test_dict[1] = "REPLACED" # Replace the value with the key of 1
print("*** Return a List of all the values in a dictionary")
print(test_dict.values())

# Find the length of the dictionary (number of key:item pairs)
dict_length = len(test_dict.values())
print(f"*** The length of the dictionary is {dict_length} items")
print("*** Use the get method for another way to return a value with a key")
print(test_dict.get(2))
# How would you make a dictionary of class members with
# email address(as the key), last name  first name and email address?
ITN1_class = {
    "fgluck@sanford.org": "Gluck, Fredric",
}

print(ITN1_class["fgluck@sanford.org"]) #Show the name of the person who owns the email

# Make a dictionary for a game that has a backpack. Use a dictionary of lists
item_value = {  # Key is player number, value is list of items in the backpack
    "FBG": ["ax", "knife"],
    "TJG": ["knife", "water"]
}
# This list will allow you to figure out the points for each item in the backpack
points = {
    "ax": 23,
    "knife": 44
}

# From Python QOD
game_pieces = {
    "Chess": 32,
    "Checkers": 24,
    "Othello": 64,
    "Deck of Cards": 52,
    "Mancala": 48
}
# What is the correct way to retrieve the number of pieces for the game Mancala?
print (f"The number of pieces for Mancala is: {game_pieces['Mancala']}")

# Iterate through a dictionary
ghosts = {
        "Red Ghost" : "Blinky",
        "Pink Ghost" : "Pinky",
        "Blue Ghost" : "Inky",
        "Orange Ghost" : "Clyde"
}

for ghost in ghosts:
    print(ghosts[ghost])

# Update a value in a dictionary

# Initialize the dictionary
number_of_transactions = {
    "amex":0,
    "visa":0,
    "mc":0
}
print (F"Total CC charges: {number_of_transactions.values()}")
# Update the items in the dictionary
number_of_transactions["amex"] = 22
number_of_transactions["visa"] = number_of_transactions["visa"] +  10
print(f"After Updating the dictionary ...")

# Raw printing of the contents of the dictionary
print (f"Total CC charges: {number_of_transactions.values()}")

# Iterate through the dictionary and print the key value pairs in a nice way
print(f"\n**Pretty Print The Contents of a Dictionary**")
print(45*'-','\n')
print(f"{'CC Type':^10}{'# of Transactions':>20}") # Header
print(f"{'----------'}{'-----------------':>20}") # Header
for i in number_of_transactions:
    print(f"{i:<10}{number_of_transactions[i]:>13}")
#    print(f"{'The Left Aligned String!!!' : <30}")
print (2*"\n")