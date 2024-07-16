def display_menu():
# This function displays the menu
# args input: none
# returns: string menu choice
    validChoice = ["1","2","3","0"]
    print("\n**********************")
    print ("[1] Greeting")
    print ("[2] Simulate Coin Flipping")
    print ("[3] Something else")
    print ("\n")
    print ("[0] Exit The Program")
    print("\n**********************")
    choice = input("What is your choice? >> ")
    if choice in validChoice:
      return choice
    else:
      return (-1)
#End of Function Defs

menuSelection = display_menu()
if menuSelection == -1:
   print ("INVALID CHOICE")
else:
   print (f"Your choice from the menu was {menuSelection} and it was a valid choice.")
