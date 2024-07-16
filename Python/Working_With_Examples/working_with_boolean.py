# Demonstration of Boolean
# True and False (Initial Caps) are keyword values
# Don't confuse them with TRUE and FALSE which are constants
# that have to have a value assigned to them.

# Not Equal Operator
var = 0  # Assigning 0 to var
print("var is: ", var, "and is var not equal to 0", var != 0)

var = 1  # Assigning 1 to var
print("var is: ", var, "and is var not equal to 0", var != 0)
print(var != 0)

# Two line program from Lab 3.1.6
n = int(input("Input a number n: "))
print(
    f"Is n <100? The answer is: {n < 100}.\nIs n >=100? The answer is: {n >= 100}.")

input("Enter to continue...")
light_switch = True
if light_switch:  # Using a boolean in a conditional statement
    print(f"The light switch is ON")
else:
    print(f"The light switch is OFF")

light_switch = False
if light_switch:  # light_switch is True
    print(f"The light switch is ON")
else:  # light_switch is FALSE
    print(f"The light switch is OFF")
