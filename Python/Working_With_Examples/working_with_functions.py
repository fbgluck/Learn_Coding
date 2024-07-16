# functions
# ref: https://www.programiz.com/python-programming/function
# define a function
# The program consists of calling each function
# Author: Fredric Gluck
# ------------------------------
# Variables


# Functions

# Demonstration Function:
# Input Params: Value for function
# Returns: Result of function
def mr_glucks_function(x):
    result = ((2*x)-8)**(2/3)
    return result
# End of Function

# Define a  basic function to calculate the area of a rectangle
# Arguments: length and width of the field
# Returns: area (integer)


def fn_field_area(area_length, area_width):
    return (area_length * area_width)


def fn_is_it_boiling(water_temp):
    # Simple function that demonstrated passing parameters, returning a value and
    # a function that behaves differently based on the parameters passed to it. (AP requirement)
    # Checks to see if water is boiling
    #
    # Input parameters: water_temp = the current temp of the water
    # ** For APCSP -- this is a function where the value of the parameter passes
    # ** effects the behavior of the function
    # Returns True if the water is boiling or False if the water is not boiling.
    if water_temp >= 212:
        print(f"Water is boiling :) ")
        return True
    else:
        print(f"Water is not boiling yet :(  ")
        return False


def absolute_value(num):
    # The following is a doc string. It is used to
    # document the purpose of a function.
    # from the Python interpreter, type -- print (absolute_value.__doc__)
    """This function returns the absolute
    value of the entered number"""

    print("\nAbsolute Value Function")
    if num >= 0:
        return num
    else:
        return -num
# End of the function because the next line is not indented

# A fancier version of the absolute value function


def fancy_av(prompt, num):
    print("\nFancy Absolute Value Function")
    if num >= 0:
        x = prompt + " " + str(num)
        return x
    else:
        return -num

# This function calculates the number of quarters you will get based
# on the bill you insert in the machine


def change_machine(amount_inserted):
    return (amount_inserted/.25)


# ----------End of Function Defs ----------------------------
# -----------------------------------------------------------

#  Main Program Starts Here
print("Mr. Gluck's Function")
for i in range(0, 11):
    print(f"The input is: {i}....The result is {mr_glucks_function(i)}")
input("Enter to continue ...")
print(30*'-')


# Ask the user for the length and width
# Call the function and return the value
user_length = int(input("What is the length of the field? >> "))
user_width = int(input("What is the width of the field? >> "))
print(f'Calling function from main program')

# We call the function here
total_area = fn_field_area(user_length, user_width)
print(f'We are back in the main program')
print(f'The area of the field is: {total_area}')
print(30*'-')
input('Enter to continue....')
# Now we will call the other functions

print(fancy_av("\nThe absolute value is: ", 2))
print(absolute_value(-4))

# - Testing the boiling water function
water_temp = int(
    input("What is the temperature of the water (degrees F) now? "))
if fn_is_it_boiling(water_temp):
    print("Hooray. Put in the noodles! ")
else:
    print("Wait a bit longer for perfect pasta. ")
