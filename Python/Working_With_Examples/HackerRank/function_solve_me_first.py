#Function Description
# REF: https://www.w3schools.com/python/python_functions.asp
# Complete the solveMeFirst function in the editor below.
#
# solveMeFirst has the following parameters:
#
# int a: the first value
# int b: the second value
# Returns
# int: the sum of a and b

def solveMeFirst(a,b):
    return(a+b)

# Use the * notation when you are not sure how many arguments are going to be passes.
# The arguments passed are placed in the tuple named after the * 
def solveMeFirst1(*args):
    return args[0] + args[1]

# Keyword Arguments
def solveMeFirst2(firstOp,secondOp):
    return(firstOp + secondOp)
# ---------------------- END OF FUNCTION DEFS -----------------

print(f"Program starts here...")
first = int(input("What is the first number"))
second =int(input("What is the second number"))

# Demo of different ways to call functions
print(f"\n ****Call by passing parameters")
print(f"The sum of {first} and {second} is {solveMeFirst(first,second)}")

print(f"\n **** Now we call with * arguments")
print(f"* ARGS: The sum of {first} and {second} is {solveMeFirst1(first,second)}")

print(f"\n**** Call by Keyword")
print(f"KEYWORD: The sum of {first} and {second} is {solveMeFirst2(firstOp = first,secondOp = second)}")
    