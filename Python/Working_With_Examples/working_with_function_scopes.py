# Working_with_function_scopes

# ENDURING UNDERSTANDINGS:
# -----------------------------
# A variable existing inside the function only has
# scope inside the function.
# What happens in functions, stays in functions!

# A variable existing outside a function has scope
# inside the function's body, excluding those which
# define a variable of the same name.
#

# ----- Function Definitions ----

def test_scopes():
    in_scope = 4
    return (in_scope)


def test_scopes_2(x):
    print(f"Inside function...x = {x}")
    x = x**x  # x is a local variable
    print(f"x raised to itself = {x}")
    return (x)


def fun():
    global a  # Make this available everywhere
    a = 2
    print(a)


#  ***** Main Program begins here *****
print("---- MAIN PROGRAM BEGINS -----")

# ---------- Part 1 ------------------------
# See PE Section 4.4.5 - Question 4
# Text has this code is a different order.. Not good
# practice. Define your functions  BEFORE you execute
# statements

a = 1
fun()
a = 3
print(a)

input("Enter to continue ...")
print(30*"-")
# --------------- Part 2 ---------------------
# print(in_scope)  # Why will we get an error here? Comment to run
print(test_scopes)
x = 5  # gloal variable. Declared at the outer level
print(f"Return from function with {test_scopes_2(x)}")
print(f"The value of x is: {x}")
print(30*"-")
