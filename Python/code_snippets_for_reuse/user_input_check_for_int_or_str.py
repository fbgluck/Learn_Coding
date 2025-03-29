# challange_visual_binary_sort_using_bar_graph
# This program demonstrates bubble sort and how to visualize it using a vertical bar chart
# Author: Fredric Gluck
# Version: 1
# ------------

# FUNCTIONS: 
# Ask user for input. Check for valid input
# arguments: prompt - printed to the user / inputType - int for integer. Others default to string (no conversion attempted)
def askForInput (prompt,inputType):
    if inputType =="int": #processing input expected to be an integer
        continueCheck = True
        while continueCheck:
            try:
                response = int(input(prompt)) # ask for input using prompt passed in. Try to convert to integer
                return(response) # successfully converted input into an integer.
            except: # couldn't convert input into integer        
                print (f"Sorry, you did not enter an integer.")

                tryAgainInput = input ("Would you like to try again? (Y or N)>> ")
                tryAgainInputLower = tryAgainInput.lower()
                if tryAgainInputLower[0]!="y": # user did not enter Y or y or Yes
                    continueCheck = False # stop the checking or y or n
        response=False # User entered no to end the check
        return response
    else: # processing input expected to be a string
        response = input(prompt)
        return response



## Program starts here
number = askForInput("Please enter an integer >> ","int")

# They did not enter a number.
if not number:
    print ("Thanks for trying")
else:
    print(f"You entered the integer {number}")