# Sample try / except / else used to handle errors
#
# ENDURING UNDERSTANDING:
# Users will always do something wrong if given a chance
# Errors should always be handled in a way that
# the end user:
# - Understands what they did wrong
# - Understands what not to do
# -
#
# This shows a reasonable way to handle errors that are
# raised in Python.
#
# ref: https://www.programiz.com/python-programming/exceptions
# ref: https://docs.python.org/3/library/exceptions.html

# The ** try ** block lets you test a block of code for system (not logic)errors.
# The ** except ** block lets you handle the error.
# The ** else ** block lets you execute code when there is no error.
# The ** finally ** block lets you execute code, regardless of the result of the try- and except blocks.'''
print("Start test...")
try:
    item = 3/0  # Force an divide by 0 system error
except:
    print("Nope... you can't divide by 0...")
else:
    print("Yep, we can do that")
finally:
    print("I'm going to do this block regardless of what happens")

input("Enter to continue...")

try:  # This is the code that will be executed
    x = input(" Enter a letter (to throw an error) or a number: ")
    x = int(x)  # This will throw a system error if a string is entered

except Exception as e:  # Optional: Uses the Exception object that is created
    # when a system occurs
    # If an error occurs in the try part, the
    # code in the except part will be executed
    print("ERROR: Python can't convert a character to an integer")
    print("Did you enter a letter when you should have entered a number?")
    print(f"Oops! {e.__class__} occurred.")  # Print the type of error
    print(f"For more info, see https://docs.python.org/3/library/exceptions.html")

else:   # If the code in try does not throw an error
    # the code in else is executed
    print(f"Coversion from string to integer was successful: x={x}")
finally:    # This code is executed regardless of the result of the code in try
    print(f" \n*** This is the code in the finally clause ***")
