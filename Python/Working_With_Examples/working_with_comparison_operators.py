# Age is the age of the customer
age = 23
# Check to see if the customer can be served
if age < 21:
    print("Underage")  # Underaged people can not be served
else:
    print("OK to serve")
print("-"*30)
# Get a number from the console to see if a number is even or odd
# Remember: all input from the console is type = string
# so we convert it to and integer before assigning it to the
# variable test
test = int(input("What is the number you want to test? "))
# Modulo operator returns the remainder
# Use the == (not =) because we are doing a comparison
if test % 2 == 0:
    print("the number", test, "is even")  # remainder is 0
else:
    print("the number", test, "is odd")  # remainder is not 0

print("-"*30)


# Order of Operations
print("Show order of operations using the same 3 variables", end="\n\n")
a = 5
b = 6
c = 7
# Why do I get different results? It's because of OOO
print("Without ():", a*b+c)
print("With ():", (a*b)+c)
print("And a different answer because of OOO:", a*(b+c))
print("-"*30)
# The "inside out" rule
print("The Inside Out Rule...")
print(15 - 1 * (5 * (1 + 2)))
print("-"*30)
# Demonstration of Order of operations
print(9 % 6 % 2)
# The statement below is the same as the statement above
print((9 % 6) % 2)
print("-"*30)
# What is the expected output?
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
# -4 goes into 2 0 times with a remainder of -2
# 4 goes into 2 0 times with a remainder of 2
print(2/-4)
print(2/4)
print(2**(3**2))
print("-"*30)
print("This statement will throw an error... WHY?")
# Why does this statement throw an error?
print(9 % (6 % 2))
