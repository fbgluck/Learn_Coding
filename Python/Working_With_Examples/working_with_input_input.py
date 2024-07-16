# This program demonstrated input and output
# Author: Fredric Gluck
# Date: 18 March 2024
# Version: 1
# --------------------------------------------------
# Start by demonstrating the print command
print ("Hello World") #This is another comment

#print("Hello",my_name) #prints their name on the screen

#print(5)
#print("5")
#my_name=input("What is your name?")
#print("This is", my_name, "Today is")

#Problem # 1
# Ask for the user name and assign it to a variable
my_name=input("What is your name? ") #Asks the user for their name
# Ask what year the user was born and assign it to a variable
birth_year = input("What year were you born? ")
birth_year_int = int(birth_year) # Converts the string input to an integer and assigns it to a new variable
# Figure out how old the user is
your_age = 2024 - birth_year_int 
#print a message that shows the results
# print ("Good morning", my_name, "You are", your_age, "today.") # # Python Unformatted Printing
print (f"Good morning {my_name}. You are {your_age} today.") # Python Formatted Printing