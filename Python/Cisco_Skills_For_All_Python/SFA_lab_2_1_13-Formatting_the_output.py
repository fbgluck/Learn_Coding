# SFA Python Part 1: Lab 2.1.13...
# Author: Fredric Gluck
# Date" 30 April 2022
#
# **** Here is the base output ****
print ("This is the base output")
print("-----------------------------------------------------------")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
print("-----------------------------------------------------------")
# **** Use a minimum number of print statements display the same figure *****
print("Do the same thing with a minimum number of print statements")
print("-----------------------------------------------------------")
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")
print("-----------------------------------------------------------")
# **** Make the arrow twice as large but keep the proportions ****
print("-----------------------------------------------------------")
print("Make the arrow twice a large but keep the proportions")
print("-----------------------------------------------------------")
# The sep argument is required because by default, print will output a space after each argument.
print(" "*9,"*",sep="")
print(" "*8,"*"," ","*",sep="")
print(" "*7,"*"," "*3,"*",sep="")
print(" "*6,"*"," "*5,"*",sep="")
print(" "*5,"*"," "*7,"*",sep="")
print(" "*4,"*"," "*9,"*",sep="")
print(" "*3,"*"," "*11,"*",sep="")
print(" "*2,"*"," "*13,"*",sep="")
print(" "*1,"*"," "*15,"*",sep="")
print("*"*6," "*7,"*"*6,sep="")
# I added a for loop even though we haven't learned about it yet
for counter in range (1,7):
    print (" "*5,"*"," "*7,"*",sep="")
print(" "*5,"*"*9,sep="")
print("-----------------------------------------------------------")
#**** Duplicate the initial arrow side by side ****
print("Print two arrows side by side")
print("-----------------------------------------------------------")
print("    *     " * 2)
print("   * *    " * 2)
print("  *   *   " * 2)
print(" *     *  " * 2)
print("***   *** " * 2)
print("  *   *   " * 2)
print("  *   *   " * 2)
print("  *****   " * 2)