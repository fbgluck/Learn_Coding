# challange_visual_binary_sort_using_bar_graph
# This program demonstrates bubble sort and how to visualize it using a vertical bar chart
# Author: Fredric Gluck
# Version: 1
# ------------

# LIBRARIES
import random

# FUNCTIONS: 
# Ask user for integer input. Check for valid input
def askForInput (prompt,inputType):
    if inputType =="int": #processing input expected to be an integer
        continueCheck = True
        while continueCheck:
            try:
                response = int(input(prompt)) # ask for input using prompt passed in
                return(response) # successfully converted input into an integer.
            except: # couldn't convert input into integer        
                print (f"Sorry, you did not enter an integer.")

                tryAgainInput = input ("Would you like to try again? (Y or N)>> ")
                tryAgainInputLower = tryAgainInput.lower()
                if tryAgainInputLower[0]!="y": # user did not enter Y or y or Yes
                    continueCheck = False # stop the checking or y or n
        response=False
        return response
    else: # processing input expected to be a string
        response = input(prompt)
        return response
# ----------------------------------------------------------
## Program starts here
listToSort = [] # start with an empty list
# Generate n random numbers into a list that will be sorted. User is asked for lower limit and upper limit of list
lowerValue = askForInput("Please enter the value of the lower limit of the range to sort >> ","int")
upperValue = askForInput("Please enter the value of the upper limit of the range to sort >> ","int")
# Now generate the list
for i in range (lowerValue, upperValue+1):
    itemToAppend = random.randint(lowerValue,upperValue)
    listToSort.append(itemToAppend)

pointer = -1 # initialize pointer
while pointer <= upperValue:
    print (listToSort) # print the bargraph of the list contents
    input("check the list to see what happend >>")
# pick the item at the pointer
    pointer = pointer + 1
# is the next item in the list < that item
    if listToSort[pointer] > listToSort[pointer+1]: # we need to swop position
        temp = listToSort[pointer+1]
        listToSort[pointer+1] = listToSort[pointer]
        listToSort[pointer] = temp
        pointer = -1

# if so, done with this round. move the starting position to the next item in the list. 
# if not, swap it with the next item    


