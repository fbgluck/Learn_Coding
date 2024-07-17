# Basics of Variables - Demonstration
# ----------------------------------------------------------
# Declaring Variable is not required. They are created and typed the first time they are used
# variable type is an integer. Use the type() function to show the variable type
firstvariable = 1
print("The variable type of firstvariable is:", type(
    firstvariable), "and its value is: ", firstvariable)
secondvariable = "myname"
print("The variable type of secondvariable is:", type(
    secondvariable), "and its value is: ", secondvariable)

# Variables can be typed when they are first used
samplestring = str("123")
print("The variable type of samplestring is", type(
    samplestring), "and it's value is:", samplestring)

samplefloat = 3.14159
print("the variable type of samplefloat is", type(
    samplefloat), "and its value is:", samplefloat)

# The dir function will show all methods of an object passed to it
# print(dir(samplefloat))

# More Examples and a shortcut for declairing multiple variables at once

test_score = 45  # snake case
myScore = 34  # Camelback
PI = 3.14  # constant
a, b, c = 1, 29, 54  # shortcut (I think this makes code harder to read)
# same as:
a = 1  # I can provide a comment for each variable describing its use
b = 29
c = 54
